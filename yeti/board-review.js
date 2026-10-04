// Aprobare / refuz / feedback per reel (db „review/reelN”) + descărcare MP4 (downloads).
(() => {
  const cards = [...document.querySelectorAll(".reel")];
  const state = {};            // id -> {status, feedback, updatedAt}
  const LABEL = { aprobat: "Aprobat", refuzat: "Refuzat", none: "Nevăzut" };
  const stateLine = document.getElementById("rvstate");
  let db = null;
  const use = n => (window.claude && window.claude.use) ? window.claude.use(n) : Promise.resolve(null);

  function paint(card) {
    const r = state[card.dataset.id] || {};
    const st = r.status || "none";
    card.dataset.st = st;
    const pill = card.querySelector(".st");
    pill.dataset.st = st; pill.textContent = LABEL[st] || LABEL.none;
    card.querySelector(".ok").setAttribute("aria-pressed", st === "aprobat");
    card.querySelector(".no").setAttribute("aria-pressed", st === "refuzat");
    const ta = card.querySelector("textarea");
    if (document.activeElement !== ta && !ta.dataset.dirty) ta.value = r.feedback || "";
  }
  function setReviewEnabled(on) {
    cards.forEach(c => c.querySelectorAll(".ok,.no,.save,textarea").forEach(el => el.disabled = !on));
  }
  setReviewEnabled(false);
  cards.forEach(paint);

  async function save(card, patch, okMsg) {
    const msg = card.querySelector(".msg");
    if (!db) { msg.textContent = "Nu pot salva aici. Deschide tabla din claude.ai, logat."; return; }
    const id = card.dataset.id;
    const ta = card.querySelector("textarea");
    const next = { status: (state[id] && state[id].status) || null, feedback: ta.value.trim(), ...patch, updatedAt: new Date().toISOString() };
    msg.textContent = "Se salvează…";
    try {
      await db.collection("review").doc(id).set(next);
      state[id] = next; delete ta.dataset.dirty; paint(card); msg.textContent = okMsg;
    } catch (e) {
      msg.textContent = e && e.code === "permission_denied" ? "Nu ai drept de scriere pe tabla asta." : "Nu s-a salvat. Mai încearcă o dată.";
    }
  }

  cards.forEach(card => {
    const ta = card.querySelector("textarea");
    ta.addEventListener("input", () => { ta.dataset.dirty = "1"; });
    card.querySelector(".ok").addEventListener("click", () => save(card, { status: "aprobat" }, "Aprobat și salvat."));
    card.querySelector(".no").addEventListener("click", () => save(card, { status: "refuzat" }, "Refuzat și salvat. Scrie-mi și ce să schimb."));
    card.querySelector(".save").addEventListener("click", () => save(card, {}, "Feedback salvat."));
    const dlBtn = card.querySelector(".dl");
    if (!card.dataset.src) { dlBtn.disabled = true; dlBtn.title = "Fișierul întreg e pe GitHub"; }
  });

  use("db").then(d => {
    if (!d) { stateLine.textContent = "Aprobarea și feedback-ul merg doar când tabla e deschisă în claude.ai."; return; }
    db = d; setReviewEnabled(true);
    db.collection("review").onSnapshot(snap => {
      snap.docs.forEach(doc => { if (doc.exists) state[doc.id] = doc.data(); });
      cards.forEach(paint);
      const n = cards.length, a = cards.filter(c => c.dataset.st === "aprobat").length, r = cards.filter(c => c.dataset.st === "refuzat").length;
      stateLine.textContent = `${a} aprobate · ${r} refuzate · ${n - a - r} de văzut`;
    }, () => { stateLine.textContent = "Nu mai primesc actualizări. Reîncarcă pagina."; });
  });

  use("downloads").then(dl => {
    cards.forEach(card => {
      const btn = card.querySelector(".dl"), msg = card.querySelector(".msg"), src = card.dataset.src;
      if (!src) return;
      btn.addEventListener("click", async () => {
        if (!dl) { const a = document.createElement("a"); a.href = src; a.download = card.dataset.file; a.click(); return; }
        btn.disabled = true; msg.textContent = "Pregătesc fișierul…";
        try {
          const blob = await (await fetch(src)).blob();
          await dl.save({ filename: card.dataset.file, data: blob });
          msg.textContent = "Descărcat.";
        } catch (e) {
          msg.textContent = e && e.code === "declined" ? "" : "Descărcarea n-a mers. Fișierul e și pe GitHub.";
        } finally { btn.disabled = false; }
      });
    });
  });
})();
