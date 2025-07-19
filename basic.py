# THIS IS NOT THE FINAL PRODUCT THIS IS JUST THE BASE IDEA
# THIS IS NOT THE FINAL PRODUCT THIS IS JUST THE BASE IDEA
# THIS IS NOT THE FINAL PRODUCT THIS IS JUST THE BASE IDEA
# THIS IS NOT THE FINAL PRODUCT THIS IS JUST THE BASE IDEA
# THIS IS NOT THE FINAL PRODUCT THIS IS JUST THE BASE IDEA
# THIS IS NOT THE FINAL PRODUCT THIS IS JUST THE BASE IDEA
# THIS IS NOT THE FINAL PRODUCT THIS IS JUST THE BASE IDEA
# THIS IS NOT THE FINAL PRODUCT THIS IS JUST THE BASE IDEA

import os
import sys
import subprocess
import tarfile
import shutil
from pathlib import Path
from urllib.parse import urlparse
import urllib.request

# Colors
w = '\033[38;2;255;255;255m'
c = '\033[38;2;140;203;255m'
g = '\033[38;2;120;255;120m'
r = '\033[38;2;255;80;80m'
reset = '\033[0m'

# Auto-install as global binary if not already
def self_install():
    target = Path("/usr/local/bin/zenith")
    current = Path(__file__).resolve()

    if not target.exists():
        print(f"{g}[+]{reset} Installing Zenith globally...")
        subprocess.run(["chmod", "+x", str(current)], check=True)
        subprocess.run(["sudo", "ln", "-sf", str(current), str(target)], check=True)
        print(f"{c}[✓]{w} Installed at {g}/usr/local/bin/zenith{reset}")
        print(f"{c}[→]{w} Re-running globally as {g}zenith{reset}\n")
        if current != target:
            os.execv(str(target), ["zenith"] + sys.argv[1:])

if not sys.argv[0].endswith("/usr/local/bin/zenith"):
    self_install()

def banner():
    print(f"""{c}

▗▄▄▄▄▖▗▄▄▄▖▗▖  ▗▖▗▄▄▄▖▗▄▄▄▖▗▖ ▗▖
   ▗▞▘▐▌   ▐▛▚▖▐▌  █    █  ▐▌ ▐▌
 ▗▞▘  ▐▛▀▀▘▐▌ ▝▜▌  █    █  ▐▛▀▜▌
▐▙▄▄▄▖▐▙▄▄▖▐▌  ▐▌▗▄█▄▖  █  ▐▌ ▐▌
    {w}Celestialis Auto Installer{reset}
    """)
    print(f"{c}[{w}*{c}]{w} Supports .deb / .tar.gz / .AppImage files")
    print(f"{c}[{w}*{c}]{w} Installing into {g}/opt{w} and symlinking to {g}/usr/local/bin{reset}\n")

def run(cmd, sudo=False):
    if sudo:
        cmd = ["sudo"] + cmd
    print(f"{c}[{w}RUN{c}]{w} {' '.join(cmd)}{reset}")
    subprocess.run(cmd, check=True)

def is_url(path):
    return path.startswith("http://") or path.startswith("https://")

def download_file(url):
    local_filename = os.path.basename(urlparse(url).path)
    print(f"{c}[{w}DL {c}]{w} Downloading {url}...{reset}")
    urllib.request.urlretrieve(url, local_filename)
    return os.path.abspath(local_filename)

def extract_tarball(file_path, install_dir="/opt"):
    name = Path(file_path).stem.replace(".tar", "")
    target_dir = os.path.join(install_dir, name)
    print(f"{c}[{w}+{c}]{w} Extracting to {g}{target_dir}{reset}")
    run(["sudo", "mkdir", "-p", target_dir])
    run(["sudo", "tar", "-xf", file_path, "-C", target_dir])
    return target_dir

def install_deb(file_path):
    print(f"{c}[{w}+{c}]{w} Installing .deb via dpkg")
    run(["sudo", "dpkg", "-i", file_path])
    run(["sudo", "apt-get", "-f", "install", "-y"])

def install_appimage(file_path, install_dir="/opt"):
    app_name = Path(file_path).stem.split("-")[0]
    target_path = os.path.join(install_dir, app_name)
    print(f"{c}[{w}+{c}]{w} Installing AppImage to {g}{target_path}{reset}")
    run(["sudo", "mkdir", "-p", target_path])
    new_path = os.path.join(target_path, Path(file_path).name)
    run(["sudo", "cp", file_path, new_path])
    run(["sudo", "chmod", "+x", new_path])
    return new_path, app_name

def symlink_binary(binary_path, name):
    link_path = f"/usr/local/bin/{name}"
    if not os.path.exists(link_path):
        print(f"{c}[{w}✓{c}]{w} Symlinking to {g}{link_path}{reset}")
        run(["sudo", "ln", "-s", binary_path, link_path])
    else:
        print(f"{c}[{w}✓{c}]{w} Symlink already exists at {link_path}{reset}")

def find_and_symlink_binary(extracted_dir, name_hint):
    print(f"{c}[{w}?{c}]{w} Looking for binary '{name_hint}'...{reset}")
    for root, _, files in os.walk(extracted_dir):
        for f in files:
            if name_hint in f and os.access(os.path.join(root, f), os.X_OK):
                full_path = os.path.join(root, f)
                symlink_binary(full_path, name_hint)
                return
    print(f"{r}[WARN]{w} Could not find binary named '{name_hint}'{reset}")

def main():
    banner()
    if len(sys.argv) < 4 or sys.argv[1] != "install":
        print(f"{r}Usage:{reset}")
        print(f"{w}  Zenith install -tar '/path/to/app.tar.gz'{reset}")
        print(f"{w}  Zenith install -deb '/path/to/app.deb'{reset}")
        print(f"{w}  Zenith install -appimage '/path/to/app.AppImage'{reset}")
        sys.exit(1)

    filetype_flag = sys.argv[2]
    file_arg = sys.argv[3]
    path = file_arg.strip().strip('"').strip("'")
    if is_url(path):
        path = download_file(path)

    if not os.path.exists(path):
        print(f"{r}[ERROR]{w} File not found: {path}{reset}")
        sys.exit(1)

    if filetype_flag == "-tar":
        extracted = extract_tarball(path)
        bin_hint = input(f"{c}[{w}?{c}]{w} Binary name to symlink (or leave blank): {reset}").strip()
        if bin_hint:
            find_and_symlink_binary(extracted, bin_hint)

    elif filetype_flag == "-deb":
        install_deb(path)

    elif filetype_flag == "-appimage":
        app_path, app_name = install_appimage(path)
        symlink_binary(app_path, app_name)

    else:
        print(f"{r}[ERROR]{w} Unsupported flag: {filetype_flag}{reset}")

    print(f"\n{g}✔ Done! You can now run your app from terminal (if symlinked).{reset}")

if __name__ == "__main__":
    main()
