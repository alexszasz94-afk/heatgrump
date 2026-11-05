"""Hook sound analysis in THREE separate parts (rule 31 Oct, Szasz), so the Kling prompt describes the sound exactly.

  python3 engine/audio3.py <hook.mp4> <hook end s> <out folder> ["<line from Higgsfield video_analysis>"] [--no-voice] [--keep-stems]

  --no-voice : the Higgsfield analysis says NOBODY speaks (song only / sounds only) -> PART 1 is skipped (otherwise
               sung lyrics come out as "words"). Rule 31 Oct, Alex.

The sound is split with Demucs (htdemucs, 4 stems in <out>/stems, deleted at the end unless --keep-stems) and every part is measured on its own:
  PART 1 VOICE      (vocals stem)          -> every word with START and END: Whisper gives the words and their order,
                                              the START is the real rising edge of the voice energy (a jump of >= 10 dB
                                              over the level just before, up to 12 dB under the word's peak) searched
                                              inside the word's own Whisper span (rule 31 Oct, Alex: Whisper's first word
                                              often says 0.00 s); loudness, pitch, length -> tone, pace, pauses, who
  PART 2 ACTIONS    (drums + other stems,  -> every short sound event (start, peak, end, loudness, low thump /
                     while nobody speaks)     mid tap / high swoosh-rustle) + a frame at each, to name the action
  PART 3 BACKGROUND (everything else)      -> per 0.5 s: its level and SILENT (dead gaps). NO music verdict (rule 31 Oct,
                                              Alex: it was wrong both ways) - check music by eye with
                                              `tools.py spectro` + the Higgsfield analysis
Writes <out>/audio3.json, <out>/events.jpg (frame at every action sound) and prints a SOUND block draft for the
Kling prompt. The Higgsfield video_analysis line (who says what) is still MANDATORY and wins on the words;
this tool gives the seconds and the delivery. Its numbers are ADVICE for the prompt and the check - they never
decide a regeneration on their own (rule 31 Oct, Alex).
"""
import json, os, shutil, subprocess, sys, tempfile
import numpy as np

SR = 16000
HOP = 160  # 10 ms


def load(p, t=None):
    cmd = ["ffmpeg", "-v", "error", "-i", p] + (["-t", str(t)] if t else []) + ["-ac", "1", "-ar", str(SR), "-f", "s16le", "-"]
    r = subprocess.run(cmd, capture_output=True).stdout
    return np.frombuffer(r, np.int16).astype(np.float32) / 32768


def env(x):
    n = len(x) // HOP
    e = np.sqrt((x[:n * HOP].reshape(n, HOP) ** 2).mean(1) + 1e-12)
    return np.convolve(e, np.ones(3) / 3, "same")


def db(v):
    return 20 * np.log10(max(float(v), 1e-6))


def separate(f, end, out):
    """Demucs stems in <out>/stems (+ mix.wav); reused when the same file and hook end were already separated."""
    sd = os.path.join(out, "stems"); os.makedirs(sd, exist_ok=True)
    stamp = os.path.join(sd, "source.txt"); key = f"{os.path.abspath(f)} {os.path.getsize(f)} {float(end):.3f}"
    names = ("mix", "vocals", "bass", "drums", "other")
    if os.path.exists(stamp) and open(stamp).read() == key and all(os.path.exists(os.path.join(sd, n + ".wav")) for n in names):
        return sd
    d = tempfile.mkdtemp(); w = os.path.join(d, "a.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f, "-t", str(end), "-vn", "-ac", "2", "-ar", "44100", w], check=True)
    subprocess.run([sys.executable, "-m", "demucs", "-n", "htdemucs", "-o", d, w], check=True, capture_output=True)
    for n in names[1:]: shutil.copy(os.path.join(d, "htdemucs", "a", n + ".wav"), sd)
    shutil.copy(w, os.path.join(sd, "mix.wav")); open(stamp, "w").write(key)
    shutil.rmtree(d, ignore_errors=True)
    return sd


def voice_onsets(ev):
    """Real starts of voice bursts (10 ms frames): the level jumps >= 10 dB above the lowest level of the 0.25 s
    before and the burst peaks within -26 dB of the clip's loudest voice; the start = first frame that reaches
    max(floor + 10 dB, burst peak - 12 dB). Returns [(start_s, peak_db)]."""
    T = len(ev); d = 20 * np.log10(ev / (ev.max() + 1e-12) + 1e-9)
    out, i = [], 1
    while i < T:
        fl = d[max(0, i - 25):i].min() if i > 0 else d[0]
        if d[i] - fl >= 10:
            pk = d[i:min(T, i + 30)].max()
            if pk >= -26:
                thr = max(fl + 10, pk - 12); j = max(0, i - 15)
                while j < T - 1 and d[j] < thr: j += 1
                if not out or j / 100 - out[-1][0] >= 0.15:
                    out.append((round(j / 100, 2), round(float(pk), 1)))
            k = i   # skip to the end of this rise (until the level falls 6 dB under the burst peak)
            while k < T - 1 and d[k] > d[i:min(T, i + 30)].max() - 6 and k < i + 60: k += 1
            i = max(k, i + 5)
        else:
            i += 1
    return out


def snap_words(raw, ev):
    """raw = Whisper words [(word, start, end)] in order. Each word gets the voice onset that lies inside its own
    Whisper span (start - 0.7 s .. end + 0.05 s), the one closest to Whisper's start, never before the previous
    word + 0.1 s. Words inside one continuous sentence (no own onset) keep Whisper's spacing, shifted like the
    sentence's first word."""
    T = len(ev); ons = voice_onsets(ev); seq = []; prev = -1.0; off = 0.0; last_e = None
    for wd, s, e in raw:
        if last_e is not None and s - last_e > 0.2: off = 0.0   # a new phrase: no inherited shift
        c = [o for o, _ in ons if s - 0.7 <= o <= e + 0.05 and o >= prev + 0.1]
        if c:
            t0 = min(c, key=lambda o: abs(o - s))
            off = t0 - s if s > 0.05 and abs(t0 - s) <= 0.4 else 0.0   # Whisper's 0.00 first word says nothing about the shift
        else:
            t0 = max(s + off, prev + 0.06)
        t0 = min(t0, T / 100 - 0.05)
        seq.append([wd, round(t0, 2), e + off]); prev = t0; last_e = e
    d = 20 * np.log10(ev / (ev.max() + 1e-12) + 1e-9)
    for k, w in enumerate(seq):   # end = the voice falls 20 dB under the word's peak, before the next word, inside the clip
        a = int(w[1] * 100); lim = int(seq[k + 1][1] * 100) - 2 if k + 1 < len(seq) else T - 1
        lim = max(min(lim, T - 1), a + 6); pk = d[a:min(lim + 1, a + 40)].max(); i = lim
        while i > a + 6 and d[i] < pk - 20: i -= 1   # last frame of the word still within 20 dB of its peak
        w[2] = round(min(max(i, a + 6), T - 1) / 100, 2)
    return [tuple(w) for w in seq]


def main(f, end, out, line="", no_voice=False, keep_stems=False):
    end = float(end); os.makedirs(out, exist_ok=True)
    st = separate(f, end, out); w = os.path.join(st, "mix.wav"); d = tempfile.mkdtemp()
    mix = load(w); voc = load(os.path.join(st, "vocals.wav"))
    bass, drums, other = (load(os.path.join(st, s + ".wav")) for s in ("bass", "drums", "other"))
    n = min(map(len, (mix, voc, bass, drums, other)))
    mix, voc, bass, drums, other = (a[:n] for a in (mix, voc, bass, drums, other))
    ev, eb, ed, eo, em = env(voc), env(bass), env(drums), env(other), env(mix)
    ref = em.max()
    T = len(ev)

    # ---------- PART 1: VOICE ----------
    words = []; seq = []
    if no_voice:
        print("PART 1 skipped (--no-voice: the Higgsfield analysis says nobody speaks)")
    else:
        try:
            from faster_whisper import WhisperModel
            import numpy as _np; _pcm = _np.ascontiguousarray(voc, dtype=_np.float32)  # 5 nov: dam direct PCM (nu fisier)
            segs, _ = WhisperModel("small.en", device="cpu", compute_type="int8").transcribe(_pcm, word_timestamps=True, language="en", beam_size=5, temperature=0.0, condition_on_previous_text=False)
            raw = [(x.word.strip(), float(x.start), float(x.end)) for s in segs for x in (s.words or [])]
        except Exception as e:
            print("WHISPER_UNAVAILABLE:", str(e)[:100]); raw = []
        seq = snap_words([x for x in raw if x[1] < T / 100 - 0.05], ev)
    import librosa
    if True:
        for wd, s, e in seq:
            a = min(int(round(s * 100)), T - 2); b = min(max(int(round(e * 100)), a + 1), T)
            x = voc[a * HOP:b * HOP]
            pk = db(ev[a:b].max() / ref) if b > a else -60
            f0 = None
            if len(x) > 1600:
                try:
                    fz, vf, _ = librosa.pyin(x, fmin=70, fmax=500, sr=SR, frame_length=1024)
                    fz = fz[~np.isnan(fz)]
                    f0 = round(float(np.median(fz))) if len(fz) else None
                except Exception:
                    pass
            words.append({"word": wd, "start": round(a / 100, 2), "end": round(b / 100, 2), "len": round((b - a) / 100, 2), "peak_db": round(pk, 1), "pitch_hz": f0})
    if words:
        pks = [x["peak_db"] for x in words]; mp = float(np.median(pks))
        for x in words:
            t = []
            if x["peak_db"] > mp + 4: t.append("louder/shouted")
            elif x["peak_db"] < mp - 6: t.append("softer")
            if x["len"] >= 0.45 and len(x["word"].strip(",.!?")) <= 6: t.append("stretched")
            x["tone"] = ", ".join(t) or "normal"
        # phrases = words separated by < 0.35 s
        phrases, cur = [], [words[0]]
        for a_, b_ in zip(words, words[1:]):
            if b_["start"] - a_["end"] < 0.35: cur.append(b_)
            else: phrases.append(cur); cur = [b_]
        phrases.append(cur)
        ph = [{"text": " ".join(x["word"] for x in p), "start": p[0]["start"], "end": p[-1]["end"],
               "words_per_s": round(len(p) / max(p[-1]["end"] - p[0]["start"], 0.1), 1)} for p in phrases]
        f0s = [x["pitch_hz"] for x in words if x["pitch_hz"]]
        who = ("high voice (woman/child)" if np.median(f0s) > 165 else "low voice (man)") if f0s else "unknown"
    else:
        ph, who = [], "nobody speaks"

    # ---------- PART 2: ACTION SOUNDS ----------
    act = eo.copy()  # drums stem = the music beat, not actions
    speaking = np.zeros(T, bool)
    for x in words:
        speaking[max(0, int(x["start"] * 100) - 5):int(x["end"] * 100) + 5] = True
    floor = np.median(act[~speaking]) if (~speaking).any() else np.median(act)
    athr = max(floor * 4, eo.max() * 10 ** (-12 / 20))
    events, i = [], 0
    S = np.abs(librosa.stft(other[:n], n_fft=1024, hop_length=HOP))
    freqs = librosa.fft_frequencies(sr=SR, n_fft=1024)
    while i < T:
        if act[i] > athr:
            j = i
            while j < T and act[j] > athr * 0.5: j += 1
            if j - i >= 3:
                pkf = i + int(np.argmax(act[i:j]))
                col = S[:, min(pkf, S.shape[1] - 1)]
                cen = float((freqs * col).sum() / (col.sum() + 1e-9))
                kind = "low thump/step" if cen < 700 else ("mid tap/knock/paper" if cen < 2500 else "high swoosh/rustle/whoosh")
                events.append({"start": round(i / 100, 2), "peak": round(pkf / 100, 2), "end": round(j / 100, 2),
                               "peak_db": round(db(act[pkf] / ref), 1), "centroid_hz": round(cen), "kind": kind,
                               "during_speech": bool(speaking[i:j].any())})
            i = j + 5
        else:
            i += 1

    # actions seen in the PICTURE (big movements = where an action sound belongs), 30 fps frame difference
    raw_v = subprocess.run(["ffmpeg", "-v", "error", "-t", str(end), "-i", f, "-vf", "fps=30,scale=64:114,format=gray", "-f", "rawvideo", "-"], capture_output=True).stdout
    fr = np.frombuffer(raw_v, np.uint8).reshape(-1, 114, 64).astype(float)
    mv = np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2)) if len(fr) > 1 else np.zeros(1)
    mthr = max(np.median(mv) * 2.5, 3.0); moves, i = [], 0
    while i < len(mv):
        if mv[i] > mthr:
            j = i
            while j < len(mv) and mv[j] > mthr * 0.6: j += 1
            pk = i + int(np.argmax(mv[i:j]))
            hard_cut = mv[pk] > 25 and (j - i) <= 2
            moves.append({"start": round((i + 1) / 30, 2), "end": round((j + 1) / 30, 2), "peak": round((pk + 1) / 30, 2),
                          "strength": round(float(mv[pk]), 1), "type": "hard cut" if hard_cut else "movement"})
            i = j + 3
        else:
            i += 1
    for e in events:
        e["matches_movement"] = any(m["start"] - 0.1 <= e["peak"] <= m["end"] + 0.1 for m in moves)

    # ---------- PART 3: BACKGROUND ----------
    bg = []
    for k in range(0, T, 50):
        sl = slice(k, min(k + 50, T))
        mus = (eb[sl].mean() + ed[sl].mean()) / (em[sl].mean() + 1e-9)
        lvl = db(np.median(em[sl]) / ref)
        # rule 31 Oct (Alex): no music verdict here any more (it was wrong both ways) - only the level and the
        # bass+drums share; music is checked by eye on `tools.py spectro` + the Higgsfield analysis.
        if lvl < -55: kind = "SILENT (dead gap)"
        else: kind = "sound"
        bg.append({"t": f"{k / 100:.1f}-{min(k + 50, T) / 100:.1f}", "kind": kind, "level_db": round(lvl, 1), "bass_drums_share": round(float(mus), 2)})
    # merge
    merged = []
    for b in bg:
        if merged and merged[-1]["kind"] == b["kind"]:
            merged[-1]["t"] = merged[-1]["t"].split("-")[0] + "-" + b["t"].split("-")[1]; merged[-1]["levels"].append(b["level_db"])
        else:
            merged.append({"t": b["t"], "kind": b["kind"], "levels": [b["level_db"]]})
    for m in merged:
        m["level_db"] = round(float(np.median(m.pop("levels"))), 1)

    # frames at every action sound
    pts = [(e["peak"], "sound " + e["kind"].split("/")[0]) for e in events] + [(m["peak"], m["type"]) for m in moves]
    pts.sort()
    if pts:
        lst = os.path.join(d, "fr"); os.makedirs(lst)
        for q, (tp, lab) in enumerate(pts[:24]):
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(tp), "-i", f, "-frames:v", "1", "-vf",
                            f"scale=240:-2,drawtext=text='{tp}s {lab}':x=4:y=4:fontsize=16:fontcolor=yellow:box=1",
                            os.path.join(lst, f"{q:02d}.jpg")])
        cols = min(6, len(pts))
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(lst, "%02d.jpg"), "-vf", f"tile={cols}x{(min(len(pts), 24) + cols - 1) // cols}",
                        "-frames:v", "1", os.path.join(out, "events.jpg")])
    shutil.rmtree(d, ignore_errors=True)
    if not keep_stems:   # rule 31 Oct (Alex): the disk is small - stems go unless --keep-stems
        shutil.rmtree(st, ignore_errors=True)

    res = {"file": f, "hook_end": end, "higgsfield_line": line, "no_voice": bool(no_voice), "part1_voice": {"who": who, "phrases": ph, "words": words},
           "part2_action_sounds": events, "part2_picture_movements": moves, "part3_background": merged}
    json.dump(res, open(os.path.join(out, "audio3.json"), "w"), indent=1, ensure_ascii=False)

    print("PART 1 VOICE -", who)
    for p in ph: print(f"  phrase {p['start']:.2f}-{p['end']:.2f}  {p['words_per_s']} words/s  \"{p['text']}\"")
    for x in words: print(f"    {x['start']:5.2f}-{x['end']:5.2f} ({x['len']:.2f}s) {x['peak_db']:6.1f} dB {str(x['pitch_hz'] or '-'):>4} Hz  {x['tone']:<22} {x['word']}")
    print("PART 2 ACTION SOUNDS (name each from events.jpg)")
    for e in events: print(f"  {e['start']:5.2f}-{e['end']:5.2f} peak {e['peak']:5.2f} {e['peak_db']:6.1f} dB {e['kind']}" + ("  (during speech)" if e["during_speech"] else ""))
    print("PART 2b MOVEMENTS IN THE PICTURE (each one gets its action sound at these seconds; name it from the frames)")
    for m in moves: print(f"  {m['start']:5.2f}-{m['end']:5.2f} peak {m['peak']:5.2f} strength {m['strength']:5.1f}  {m['type']}")
    print("PART 3 BACKGROUND (music: check `tools.py spectro` + the Higgsfield analysis, not this list)")
    for m in merged: print(f"  {m['t']:>9} s  {m['kind']:<22} {m['level_db']} dB")
    print("\nSOUND block draft (name each action sound from events.jpg; music is never asked for):")
    acts = "; ".join(f"at {m['start']}-{m['end']} s <sound> as <action>" for m in moves if m["type"] == "movement") or "<none>"
    gaps = [m["t"] for m in merged if m["kind"].startswith("SILENT")]
    if words:
        vparts = "; ".join(f"\"{x['word']}\" from {x['start']} s to {x['end']} s" + (f" ({x['tone']})" if x['tone'] != 'normal' else "") for x in words)
        voice = (f"VOICE (layer 1): {who}, <tone>, lips in perfect sync. She says ONLY these words, each word starting exactly on its second: {vparts}. "
                 f"After \"{words[-1]['word']}\" nobody says anything else. No other words, no other voice, no narrator, no whisper. ")
    else:
        voice = "VOICE (layer 1): nobody speaks - no voice, no words, no humming. "
    print("SOUND - made by you, with the picture, in three layers. ABSOLUTELY NO MUSIC: no song, no beat, no melody, no instruments, no jingle bells, no humming. "
          + voice + f"ACTION SOUNDS (layer 2), exactly when they happen in the picture: {acts}. "
          "BACKGROUND (layer 3): from 0 s to the end only the quiet room tone of <OUR place> (<details>), continuous, never silent, never louder than the voice.")
    if gaps: print("NOTE: dead-silent parts in this clip at", gaps, "s (if this is OUR hook: `tools.py roomtone`)")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a not in ("--no-voice", "--keep-stems")]
    if len(args) < 3:
        print(__doc__); sys.exit(1)
    main(*args[:4], no_voice="--no-voice" in sys.argv[1:], keep_stems="--keep-stems" in sys.argv[1:])
