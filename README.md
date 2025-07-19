
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

## License
MIT License - freely usable, modifiable, and distributable

---

> **Release Timeline**  
> The public repository and production-ready install script will be available in August 2025.  
> This documentation represents the final pre-release specification.
