"""
fix_repo.py — Run this inside your cloned OTT-DOWNLOADER folder.
It reorganizes all files into the correct folder structure and
creates any missing platform scripts.

Usage:
    cd OTT-DOWNLOADER
    python fix_repo.py
"""

import os
import shutil
from pathlib import Path

ROOT = Path(__file__).parent

# ── Folders to create ──────────────────────────────────────────────────────
DIRS = [
    "scripts/global",
    "scripts/indian",
    "scripts/regional",
    "utils",
    "config",
    "docs",
    "output/movies",
    "output/shows",
    "output/anime",
    "output/documentaries",
    "logs",
    ".github/workflows",
    "cookies",
]

# ── Files that belong in utils/ ────────────────────────────────────────────
UTIL_FILES = [
    "downloader.py",
    "logger.py",
    "naming_convention.py",
    "cookies.py",
    "manifest_parser.py",
    "post_processor.py",
    "subtitle_handler.py",
    "__init__.py",
]

# ── Files that belong in scripts/ root ─────────────────────────────────────
SCRIPT_ROOT_FILES = [
    "single_rip.py",
    "run_all.py",
]

# ── Platform scripts to generate ───────────────────────────────────────────
GLOBAL_PLATFORMS  = ["netflix","prime","disney","hbomax","hulu","apple","peacock","paramount"]
INDIAN_PLATFORMS  = ["hotstar","jiocinema","sonyliv","zee5","altbalaji","erosnow","manoramamax","hoichoi"]
REGIONAL_PLATFORMS= ["aha","mxplayer","voot","shemaroo","sun_nxt","yupp_tv","stage"]

PLATFORM_SCRIPT = '''"""
{name} — OTT ripper script.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from utils.downloader import download
from utils.cookies import get_cookie_path

PLATFORM = "{plat}"


def rip(url: str, quality: str = "{quality}", content_type: str = "movies", **kwargs):
    cookie_file = get_cookie_path(PLATFORM)
    return download(
        url=url,
        platform=PLATFORM,
        content_type=content_type,
        quality=quality,
        cookie_file=cookie_file,
        **kwargs,
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=f"Rip from {name}")
    parser.add_argument("--url",     required=True)
    parser.add_argument("--quality", default="{quality}")
    parser.add_argument("--type",    default="movies")
    args = parser.parse_args()
    rip(args.url, quality=args.quality, content_type=args.type)
'''

GITKEEP_CONTENT = ""  # empty placeholder so git tracks empty dirs

COOKIES_GITKEEP = """# Place your platform cookie files here.
# Filename format: <platform>.txt  (Netscape cookies format)
# Examples:
#   netflix.txt
#   jiocinema.txt
#   hotstar.txt
#
# Export cookies using the browser extension:
# "Get cookies.txt LOCALLY" (Chrome / Firefox)
#
# This folder is in .gitignore — your cookies will NOT be uploaded to GitHub.
"""

GITHUB_WORKFLOW = """name: Lint & Syntax Check

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install deps
        run: pip install flake8
      - name: Lint
        run: flake8 scripts/ utils/ --max-line-length=100 --ignore=E501,W503
"""

# ── Step 1: Create all directories ─────────────────────────────────────────
print("\\n📁 Creating folder structure...")
for d in DIRS:
    (ROOT / d).mkdir(parents=True, exist_ok=True)
    print(f"   ✓ {d}/")

# ── Step 2: Move util files to utils/ ──────────────────────────────────────
print("\\n📦 Moving utility files → utils/")
for fname in UTIL_FILES:
    src = ROOT / fname
    dst = ROOT / "utils" / fname
    if src.exists() and not dst.exists():
        shutil.move(str(src), str(dst))
        print(f"   ✓ moved {fname} → utils/{fname}")
    elif dst.exists():
        print(f"   – utils/{fname} already in place")
    else:
        print(f"   ? {fname} not found at root (may already be moved)")

# utils __init__
init = ROOT / "utils" / "__init__.py"
if not init.exists():
    init.write_text('"""OTT Ripper utilities."""\n')
    print("   ✓ created utils/__init__.py")

# ── Step 3: Move entry-point scripts to scripts/ ───────────────────────────
print("\\n🚀 Moving entry-point scripts → scripts/")
for fname in SCRIPT_ROOT_FILES:
    src = ROOT / fname
    dst = ROOT / "scripts" / fname
    if src.exists() and not dst.exists():
        shutil.move(str(src), str(dst))
        print(f"   ✓ moved {fname} → scripts/{fname}")
    elif dst.exists():
        print(f"   – scripts/{fname} already in place")

scripts_init = ROOT / "scripts" / "__init__.py"
if not scripts_init.exists():
    scripts_init.write_text("")

# ── Step 4: Generate platform scripts ──────────────────────────────────────
print("\\n🌍 Generating global platform scripts...")
for plat in GLOBAL_PLATFORMS:
    path = ROOT / "scripts" / "global" / f"{plat}.py"
    if not path.exists():
        path.write_text(PLATFORM_SCRIPT.format(name=plat.capitalize(), plat=plat, quality="1080p"))
        print(f"   ✓ scripts/global/{plat}.py")

print("\\n🇮🇳 Generating Indian platform scripts...")
for plat in INDIAN_PLATFORMS:
    path = ROOT / "scripts" / "indian" / f"{plat}.py"
    quality = "4K" if plat == "jiocinema" else "1080p"
    if not path.exists():
        path.write_text(PLATFORM_SCRIPT.format(name=plat.capitalize(), plat=plat, quality=quality))
        print(f"   ✓ scripts/indian/{plat}.py")

print("\\n🗺️  Generating regional platform scripts...")
for plat in REGIONAL_PLATFORMS:
    path = ROOT / "scripts" / "regional" / f"{plat}.py"
    if not path.exists():
        path.write_text(PLATFORM_SCRIPT.format(name=plat.capitalize(), plat=plat, quality="720p"))
        print(f"   ✓ scripts/regional/{plat}.py")

# __init__ files for subpackages
for sub in ["global", "indian", "regional"]:
    p = ROOT / "scripts" / sub / "__init__.py"
    if not p.exists():
        p.write_text("")

# ── Step 5: Gitkeep placeholders for output/logs/cookies ───────────────────
print("\\n📝 Adding .gitkeep placeholders...")
for folder in ["output/movies","output/shows","output/anime","output/documentaries","logs"]:
    gk = ROOT / folder / ".gitkeep"
    if not gk.exists():
        gk.write_text(GITKEEP_CONTENT)
        print(f"   ✓ {folder}/.gitkeep")

(ROOT / "cookies" / "README.txt").write_text(COOKIES_GITKEEP)
print("   ✓ cookies/README.txt")

# ── Step 6: GitHub Actions workflow ────────────────────────────────────────
wf = ROOT / ".github" / "workflows" / "lint.yml"
if not wf.exists():
    wf.write_text(GITHUB_WORKFLOW)
    print("\\n⚙️  Created .github/workflows/lint.yml")

# ── Step 7: Update .gitignore ──────────────────────────────────────────────
gitignore_path = ROOT / ".gitignore"
gitignore_content = """# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/
env/

# Credentials & cookies — NEVER commit
cookies/*.txt
config/settings.yaml
.env

# Output & logs
output/
logs/
*.mkv
*.mp4
*.ts
*.m4v
*.srt
*.ass
*.vtt

# DRM keys
*.wvd
keys/
cdm/

# OS
.DS_Store
Thumbs.db
"""
gitignore_path.write_text(gitignore_content)
print("\\n🔒 Updated .gitignore")

# ── Done ───────────────────────────────────────────────────────────────────
print("\n" + "="*55)
print("✅  Reorganisation complete!")
print("="*55)
print("""
Now run these commands to push everything to GitHub:

  git add .
  git commit -m "refactor: reorganise into proper folder structure"
  git push origin main

Your repo will then match the structure shown in README.md
""")
