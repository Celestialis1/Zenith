# Zenith
> ⚠️ **Notice:**  
> Source code will be released after final polish and testing — planned for next month.


**Zenith** is a lightweight, universal Linux app installer. It supports `.AppImage`, `.deb`, `.tar.gz`, `.snap`, `.flatpak`, and URL-based installs — with smart binary linking and local tracking.

Think of it as a user-friendly package handler for non-repo applications.

---

## ✨ Features

- 🗃️ Handles `.appimage`, `.tar.gz`, `.deb`, `.snap`, `.flatpak`, and direct URLs
- 📦 Auto-detects and links binaries to `/usr/local/bin`
- 📋 Tracks installations in a local JSON database
- 🔁 Self-updates (`zenith update`)
- 🚀 Simple commands: `install`, `list`, `uninstall`, `config`
- 💡 Minimal dependencies, no root required (except for system installs)

---

## 📦 Installation

### Manual

```bash
git clone https://github.com/Celestialis1/Zenith
cd zenith
python3 zenith.py self-install
````

### Or Run Ad-Hoc

```bash
python3 zenith.py install <target>
```

Example:

```bash
python3 zenith.py install -deb ~/Downloads/code.deb
```

---

## 🛠 Usage

### Basic Install

```bash
zenith install <file_or_url>
```

### Install Flags

| Flag        | Description                         |
| ----------- | ----------------------------------- |
| `-deb`      | Force `.deb` install                |
| `-tar`      | Force `.tar.gz` install             |
| `-appimage` | Force `.AppImage` install           |
| `-flatpak`  | Flatpak file or ID                  |
| `-snap`     | Snap file or app ID                 |
| `-url`      | Direct download from URL            |
| `-auto`     | Auto-detect type (default behavior) |

### Other Commands

```bash
zenith list             # Show installed apps
zenith uninstall <app>  # Remove app and references
zenith config           # Edit the config JSON
zenith self-update      # Update Zenith to latest version
zenith help             # Show usage info
```

---

## 🔍 Example

```bash
zenith install https://downloads.slack-edge.com/linux_releases/slack-desktop-4.35.131-amd64.deb
zenith install -appimage ~/Downloads/Obsidian-1.5.3.AppImage
```

---

## 🧾 Config

Zenith stores settings and install metadata in:

```
~/.config/zenith/
├── config.json
└── installed.json
```

You can customize install paths, default behavior, and more by editing `config.json`.

---

## 🧰 Requirements

* Python 3.7+
* `requests`, `tqdm`, `colorama`, `rich`
* Optional: `python-magic` (for MIME type fallback)

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## 📎 Roadmap

* [ ] Github Release
* [ ] Application Icons
* [ ] Manifest files (`.zenith.json`)
* [ ] Plugin system for custom install logic
* [ ] `.desktop` launcher generation (optional)
* [ ] GUI frontend

---

## 📜 License

MIT — free to use, modify, and share.

---

```bash
sudo rm -rf complexity
```
