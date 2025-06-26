# 🎧 Capsize

Capsize is a DJ-focused desktop app that syncs playlists from Spotify, SoundCloud, Apple Music, and YouTube into high-quality, locally stored audio files — optimized for Rekordbox integration. It prioritizes accurate syncing, minimal storage duplication, and a clean user experience.

---

## 🚀 Features

- 🔗 OAuth login for Spotify, SoundCloud, Apple Music
- 🎵 Sync playlists and songs with accurate metadata
- 🗃️ Deduplicated audio storage with symlinks for playlist views
- 🎚️ High-quality audio download (320kbps MP3 or better)
- 🎛️ Rekordbox-compatible folder structure
- 🔁 Change detection and incremental sync
- 💾 Local SQLite database — no cloud backend
- 🧼 Clean, dark-mode UI (Electron + React + Tailwind)

---

## 🏗️ Tech Stack

| Layer       | Tech                                 |
|-------------|--------------------------------------|
| Frontend    | React + TypeScript + Tailwind CSS    |
| Shell       | Electron (macOS only for now)        |
| Backend     | Python Flask API                     |
| Database    | SQLite + SQLAlchemy ORM              |
| Downloader  | yt-dlp or similar                    |
| OAuth APIs  | Spotify, SoundCloud, Apple Music     |

---

## 📁 Folder Structure

```bash
capsize/
├── backend/       # Flask API
├── frontend/      # React + Tailwind
├── electron/      # Electron main & preload
├── data/          # Local audio and playlist folders
├── .env           # Env config
├── README.md
```

---

## 🛠️ Development Plan

1. ✅ Define requirements & UI in Figma
2. ✅ Scaffold project directory
3. 🔄 Build and migrate SQLite schema
4. 🔄 Integrate Spotify OAuth & playlist fetcher
5. 🔄 Implement download + metadata injection
6. 🔄 Build React UI with playlist management
7. 🔄 Connect Electron shell and wrap it all

---

## 📦 Setup (WIP)

To run this app locally:

```bash
# Backend
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run

# Frontend
cd frontend
npm install
npm run dev

# Electron
cd electron
npm install
npm run electron
```

(Setup scripts coming soon)

---

## ⚠️ Platform Support

- ✅ macOS (primary target)
- ⏳ Windows/Linux support TBD
- Rekordbox integration confirmed on macOS with symlinks

---

## 🧠 About the Name

Capsize: a tip of the hat to DJs flipping the boat with killer sets.  
It’s all about full control, minimal friction, and smooth sailing.

---

## 📝 License

[MIT](LICENSE)

---

Capsize is an independent passion project built for DJs who want precision, quality, and control — without jank.  
PRs, issues, or feedback welcome. Let’s build something clean.
