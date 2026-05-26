<div align="center">

```
 ██████╗ ████████╗████████╗    ██████╗ ██╗██████╗ ██████╗ ███████╗██████╗ 
██╔═══██╗╚══██╔══╝╚══██╔══╝    ██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║   ██║   ██║      ██║       ██████╔╝██║██████╔╝██████╔╝█████╗  ██████╔╝
██║   ██║   ██║      ██║       ██╔══██╗██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
╚██████╔╝   ██║      ██║       ██║  ██║██║██║     ██║     ███████╗██║  ██║
 ╚═════╝    ╚═╝      ╚═╝       ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
```

**A unified automation toolkit to rip from every major OTT platform.**  
Movies · TV Shows · Anime · Documentaries

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square)
![Platforms](https://img.shields.io/badge/Platforms-20%2B-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

</div>

---

## 📡 Supported Platforms

### 🌍 Global OTTs
| Platform | Status | DRM | Quality |
|---|---|---|---|
| Netflix | ✅ Active | Widevine L3 | Up to 1080p |
| Amazon Prime | ✅ Active | Widevine L3 | Up to 1080p |
| Disney+ / Hotstar | ✅ Active | Widevine L3 | Up to 1080p |
| HBO Max | ✅ Active | Widevine L3 | Up to 1080p |
| Hulu | ✅ Active | Widevine L3 | Up to 1080p |
| Apple TV+ | ⚠️ Partial | FairPlay | Up to 720p |
| Peacock | ✅ Active | Widevine L3 | Up to 1080p |
| Paramount+ | ✅ Active | Widevine L3 | Up to 1080p |

### 🇮🇳 Indian OTTs
| Platform | Status | DRM | Quality |
|---|---|---|---|
| JioCinema | ✅ Active | Widevine L3 | Up to 4K |
| SonyLIV | ✅ Active | Widevine L3 | Up to 1080p |
| Zee5 | ✅ Active | Widevine L3 | Up to 1080p |
| ALTBalaji | ✅ Active | Widevine L3 | Up to 1080p |
| Eros Now | ✅ Active | Widevine L3 | Up to 1080p |
| ManoramaMAX | ⚠️ Partial | Widevine L3 | Up to 720p |
| Hoichoi | ✅ Active | Widevine L3 | Up to 1080p |

### 🗺️ Regional OTTs
| Platform | Status | Language | Quality |
|---|---|---|---|
| Aha | ✅ Active | Telugu / Tamil | Up to 1080p |
| MX Player | ✅ Active | Multi | Up to 1080p |
| Voot | ✅ Active | Hindi / Multi | Up to 1080p |
| Shemaroo | ✅ Active | Hindi | Up to 720p |
| Sun NXT | ✅ Active | Tamil / Telugu / Kannada | Up to 1080p |
| YuppTV | ⚠️ Partial | Multi | Up to 720p |
| Stage | ✅ Active | Haryanvi / Rajasthani | Up to 720p |

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/ott-ripper.git
cd ott-ripper

# Install dependencies
pip install -r requirements.txt

# Set up your cookies and config
cp config/settings.yaml.example config/settings.yaml
# Edit settings.yaml with your credentials / cookie paths

# Rip a single title
python scripts/single_rip.py --platform netflix --url "https://www.netflix.com/watch/XXXXXX"

# Rip from all platforms (batch mode)
python scripts/run_all.py --config config/batch_list.txt
```

---

## 📁 Repository Structure

```
ott-ripper/
├── scripts/
│   ├── global/          # Global OTT platform scripts
│   │   ├── netflix.py
│   │   ├── prime.py
│   │   ├── disney.py
│   │   └── ...
│   ├── indian/          # Indian OTT platform scripts
│   │   ├── jiocinema.py
│   │   ├── sonyliv.py
│   │   ├── zee5.py
│   │   └── ...
│   ├── regional/        # Regional OTT platform scripts
│   │   ├── aha.py
│   │   ├── sun_nxt.py
│   │   └── ...
│   ├── single_rip.py    # Single-title rip entry point
│   └── run_all.py       # Batch rip entry point
├── utils/
│   ├── downloader.py        # Core download engine (yt-dlp wrapper)
│   ├── manifest_parser.py   # MPD/HLS manifest parsing
│   ├── cookies.py           # Cookie extraction & management
│   ├── post_processor.py    # Mux, remux, convert (ffmpeg)
│   ├── subtitle_handler.py  # Subtitle download & conversion
│   ├── naming_convention.py # Output filename formatter
│   └── logger.py            # Logging utility
├── config/
│   ├── platforms.json       # Platform endpoints & DRM config
│   └── settings.yaml        # User settings (cookies, paths, quality)
├── output/
│   ├── movies/
│   ├── shows/
│   ├── anime/
│   └── documentaries/
├── logs/                    # Rip logs per session
├── docs/
│   ├── SETUP.md
│   ├── USAGE.md
│   ├── PLATFORMS.md
│   └── CONTRIBUTING.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Configuration

Edit `config/settings.yaml` to configure output quality, paths, and cookies:

```yaml
output:
  base_path: ./output
  quality: 1080p          # 4K / 1080p / 720p / 480p
  format: mkv             # mkv / mp4
  subtitles: true
  audio_languages: [hi, en, ta, te]

cookies:
  netflix: ./cookies/netflix.txt
  prime: ./cookies/prime.txt
  hotstar: ./cookies/hotstar.txt
  # ... add others

tools:
  yt_dlp_path: yt-dlp
  ffmpeg_path: ffmpeg
  mp4decrypt_path: mp4decrypt
  aria2c_path: aria2c
```

---

## 🛠️ Dependencies

| Tool | Purpose |
|---|---|
| `yt-dlp` | Core download engine |
| `ffmpeg` | Muxing, remuxing, conversion |
| `mp4decrypt` | Widevine L3 decryption |
| `aria2c` | Multi-connection download accelerator |
| `requests` | API calls |
| `python-dotenv` | Env variable management |
| `pyyaml` | Config parsing |
| `rich` | Terminal UI / progress bars |

Install all Python dependencies:
```bash
pip install -r requirements.txt
```

---

## 📖 Docs

- [Setup Guide](docs/SETUP.md)
- [Usage Guide](docs/USAGE.md)
- [Platform Notes](docs/PLATFORMS.md)
- [Contributing](docs/CONTRIBUTING.md)

---

## ⚠️ Disclaimer

This project is for **educational and personal use only**. Ripping DRM-protected content may violate the Terms of Service of the respective platforms and local copyright laws. The contributors are not responsible for any misuse. Use responsibly and only for content you have the right to access.

---

## 🤝 Contributing

PRs welcome! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

---

<div align="center">
Made with ❤️ for the archiving community
</div>
