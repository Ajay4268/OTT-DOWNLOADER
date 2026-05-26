# Setup Guide

## 1. System Requirements

- Python 3.10+
- `ffmpeg` installed and in PATH
- `yt-dlp` installed (`pip install yt-dlp`)
- `mp4decrypt` (from Bento4) for DRM-protected content
- `aria2c` (optional, for faster multi-connection downloads)

## 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 3. Install System Tools

### Ubuntu / Debian
```bash
sudo apt install ffmpeg aria2
pip install yt-dlp
```

### macOS (Homebrew)
```bash
brew install ffmpeg aria2 yt-dlp
```

### Windows
Download from:
- ffmpeg: https://ffmpeg.org/download.html
- yt-dlp: https://github.com/yt-dlp/yt-dlp/releases
- aria2: https://github.com/aria2/aria2/releases

## 4. Cookie Setup

Most platforms require authentication via cookies.

1. Install browser extension: **"Get cookies.txt LOCALLY"** (Chrome/Firefox)
2. Log in to the OTT platform in your browser
3. Export cookies as `cookies.txt` (Netscape format)
4. Place the file at `cookies/<platform>.txt`

Example:
```
cookies/
├── netflix.txt
├── prime.txt
├── jiocinema.txt
└── ...
```

## 5. Configure Settings

```bash
cp config/settings.yaml.example config/settings.yaml
# Edit with your preferred quality, audio languages, and tool paths
```

## 6. Test Your Setup

```bash
python scripts/single_rip.py --platform mxplayer --url "https://www.mxplayer.in/..." --quality 720p
```
MX Player has no DRM, so it's a good first test.
