
# Zenith: Universal Linux Package Installer  
**Streamlined application deployment with unified package management**  
**Public Release: August 2025** (Approximately 3–4 weeks)

---

> **Early-Access Preview Notice**  
> Source code is currently completing internal quality assurance and will be published on GitHub in August 2025.  
> This documentation reflects the finalized pre-release implementation – all described features are fully implemented and tested.

---

## Key Capabilities

| Operation | Command |
|-----------|---------|
| Install `.tar.gz`/`.tar.xz`/`.tar.bz2` (flat/nested) | `zenith install -auto <file.tar.gz>` |
| Install `.AppImage` | `zenith install -auto <app.AppImage>` |
| Install `.deb`, `.snap`, `.flatpak` | `zenith install -auto <package>` |
| Install from URL | `zenith install -auto <https://.../app.AppImage>` |
| Remove applications | `zenith uninstall <name>` |
| List installed applications | `zenith list` |
| Update installer | `zenith update` |

---

## Version 2.0 Feature Highlights

- **Permission-adaptive installation**: Automatically installs to `/opt` when permitted, otherwise uses `~/.local/zenith/apps` without requiring sudo privileges
- **Interactive installation prompts**: Configure applications as terminal or GUI during installation (sets `Terminal` property in `.desktop` files)
- **Flat tarball handling**: Automatically creates container directories for archives lacking top-level folders
- **User-space integration**: Creates executable symlinks in `~/.local/bin` (standard PATH location)
- **Icon management**: Extracts application icons from AppImages/tarballs with fallback to default icon
- **Centralized management**: Maintains installation database in `~/.zenith/`

---

## Installation and Usage

```bash
# Install Zenith
curl -sSL https://raw.githubusercontent.com/Celestialis1/Zenith/main/zenith.py \
  | sudo tee /usr/local/bin/zenith > /dev/null && sudo chmod +x /usr/local/bin/zenith

# Install application
zenith install -auto ~/Downloads/seanime-2.9.0_Linux_x86_64.tar.gz

# Execute installed application
seanime
```

---

## Filesystem Structure

| Location | Purpose |
|----------|---------|
| `~/.local/zenith/apps/` | User-space application installations |
| `~/.local/bin/` | Application binary symlinks (PATH accessible) |
| `~/.local/share/applications/` | Generated desktop entries |
| `~/.zenith/` | Configuration and installation database |
| `/opt/` | System-wide installations (when permitted) |

---

## Technical Requirements

- Python 3.7+ (standard library only)
- Recommended: `python-magic` for enhanced MIME type detection
- No external dependencies

---

## Frequently Asked Questions (FAQ)

### ❓ Does Zenith handle `.tar` files differently from `.AppImage`?

**Yes.**
AppImages are self-contained and require minimal setup. Zenith simply copies the file, sets execution permissions, and (optionally) generates a `.desktop` launcher with icon support.

`.tar` archives, however, require extraction and post-processing. Zenith:

* Detects whether the archive has a top-level directory or is flat
* Moves contents to a sandboxed location
* Searches for the main executable
* Optionally creates a launcher and icon
  Some `.tar` packages may require manual tweaks if they lack a clear structure or launcher binary.

---

### ❓ Does Zenith require `sudo` or root access?

**No, not by default.**
Zenith is designed to install everything into user-space (`~/.local/zenith/apps/`) by default.
If `sudo` is available, it offers to install system-wide to `/opt`, but this is optional and permission-aware.

---

### ❓ Can I install apps from a URL?

**Yes.**
Zenith supports direct URL installation of any supported format:

```bash
zenith install -auto https://example.com/tool.AppImage
```

It automatically detects and processes the file after download.

---

### ❓ What happens if the app has no desktop icon?

Zenith attempts to extract an icon from the application. If none is found, it falls back to a generic icon. You can later replace or edit the icon manually in `~/.local/share/applications/`.

---

### ❓ Can I remove or update apps?

* To remove:

```bash
zenith uninstall <app-name>
```

* Zenith does **not** currently auto-update individual apps, but you can re-run the install with a newer version to overwrite an old one.
* To update Zenith itself:

```bash
zenith update
```

---

### ❓ Where are installed files stored?

All user-space installs go to:

* Apps: `~/.local/zenith/apps/`
* Executables: `~/.local/bin/`
* Icons/Desktop files: `~/.local/share/applications/`
* Metadata: `~/.zenith/`

---

Let me know if you'd like to include troubleshooting tips, advanced options, or developer notes as well.

---

## License
MIT License - freely usable, modifiable, and distributable

---

> **Release Timeline**  
> The public repository and production-ready install script will be available in August 2025.  
> This documentation represents the final pre-release specification.
