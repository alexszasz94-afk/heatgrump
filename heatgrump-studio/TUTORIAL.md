# Robe Studio — full guide

**This guide is only for Claude Code on the web (claude.ai/code).** Nothing is installed on your computer.

> Short version: **START-HERE.md**. Step-by-step with every click: **SETUP.html**. How the system works: **HOW-IT-WORKS.pdf**.

You send Claude a reel link or tell it an idea, in normal words. Claude makes the whole video: the hook, a new woman in a new room putting on the robe, the connector and the heating remote, the cozy ending and the music. You get one MP4 (without text on purpose) plus the exact text to add in CapCut, in about 20–30 minutes. You don't need to know how to code and there are no commands to learn.

## Who does what
- **Alex** prepares the whole kit and sends you this guide and a folder **robe-studio-upload** with 11 files (the whole kit). About once a week he sends a small update file. Write to Alex if you're stuck.
- **You** make the accounts, do the 5 setup steps once, then talk to Claude and post the videos.

## What you need
- A **Claude** subscription (Pro or Max) — Claude Code on the web is included.
- A **Higgsfield** account with credits (higgsfield.ai) — this is where the images and videos are made.
- A free **GitHub** account (github.com) — your kit lives there and your finished videos land there.

## Setup, once (about 5 minutes)
1. **Your copy of the kit.** Download Alex's **robe-studio-upload** folder to your computer (11 files: `CLAUDE.md` and `robe-studio.zip.part-aa` … `-aj`; don't open them). On **github.com** (make a free account if needed) click **+** → **New repository**. Name: `robe-studio`. Choose **Private**. Click **Create repository**. On the next page click **uploading an existing file**, open the folder on your computer, select the 11 files inside (Ctrl+A on Windows, Cmd+A on Mac) and drag the files in — not the folder itself (the files must sit at the top of your GitHub folder). Wait until all 11 are listed, click **Commit changes**. Claude unpacks the kit by itself the first time you say hi.
2. **Connect Higgsfield.** Open **claude.ai/customize/connectors**, find **Higgsfield**, click **Connect** and log in to your Higgsfield account.
3. **Open Claude Code.** Go to **claude.ai/code**. The first time it asks to connect GitHub: allow it (give it access to `robe-studio`). Pick the `robe-studio` repository.
4. **Let it reach Instagram/TikTok.** At the top of the chat click the environment name (the cloud icon) → **Edit** → **Network access**, then pick one: **Full** (easiest: Claude may open any site) or **Custom/Limited** (stricter: leave *Allow package managers* ticked and paste the list from `setup/allowed-domains.txt` into **Allowed domains**). **Save**. You do it only once.
5. **Say hi.** Write: *Hi, set me up.* Claude checks everything, uploads the robe pictures to your Higgsfield once and tells you when it's ready. The tools it needs install themselves every time a session starts.

## Making videos — just talk
- *"Make this one with the princess robe: https://www.instagram.com/reel/…"*
- *"Can you do this TikTok with Snoopy?"*
- *"I have my own idea: she opens the front door and her mom holds a giant gift box."* → Claude shows you the first frame, you say OK and how it should move, Claude does the rest.
- Every video ends with the classic cozy shot on the sofa. Want something else? Just say it (*reading a book on the sofa*, *hot cocoa*…) — Claude doesn't wait for you to choose. Change it often.

At the end Claude gives you the video, a caption and the text to type in CapCut (top of the screen). They are also saved in your GitHub repository: open github.com → `robe-studio` → `output` → your video → **Download**.

Want a specific song? Download it as an MP3, drag it into the chat (or use the paperclip) and say *"use this song"*. Claude puts the song's big moment on the cut right after the hook.

Want a change? Say it: *"use another song"*, *"the hood looks wrong at the end"*. Claude redoes only that part.

## Updates from Alex
About once a week Alex sends a file like `robe-studio-update-2026-11-02.zip`. Open a chat, drag the file in and write *"here is the new update from Alex"*. Claude installs it and tells you what's new; your videos and history stay.

## Tips
- The best reels to copy are short (10–20 s) with a strong first 3 seconds.
- Mix: for every two or three copied reels, try one hook of your own. New hooks are what make your account stand out.
- Every video gets a new woman and a new room automatically (the kit has 40 rooms in 4K, each with a sofa). When the women run low, Claude finds new ones on Pinterest by itself; new rooms come from Alex as a zip. You can also just say *"I want new girls"*.
- Start a new chat for each new video — it keeps things fast.

## If something goes wrong
- Claude says Higgsfield is not connected → open **claude.ai/customize/connectors**, connect Higgsfield again, then start a new chat.
- Claude says a download was blocked → check step 4 (Network access; with the stricter option add the site Claude names), then start a new chat.
- Credits ran out → top up on higgsfield.ai.
- Anything else → ask *"what went wrong?"* — Claude explains and fixes it.
