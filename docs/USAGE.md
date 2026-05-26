# Usage Guide

## Single Title Rip

```bash
python scripts/single_rip.py \
  --platform jiocinema \
  --url "https://www.jiocinema.com/movies/..." \
  --quality 4K \
  --type movies \
  --audio hi en
```

### Arguments

| Argument | Options | Default | Description |
|---|---|---|---|
| `--platform` | See platforms list | required | OTT platform |
| `--url` | Any URL | required | Content page URL |
| `--quality` | 4K, 1080p, 720p, 480p | 1080p | Output quality |
| `--type` | movies, shows, anime, documentaries | movies | Content type |
| `--audio` | Language codes | hi en | Audio tracks |
| `--subs` | flag | enabled | Download subtitles |

---

## Batch Rip

Create a batch file `config/batch_list.txt`:
```
# Format: platform|url|quality|type
netflix|https://www.netflix.com/watch/12345|1080p|movies
jiocinema|https://www.jiocinema.com/movies/abc|4K|movies
aha|https://www.aha.video/...|1080p|shows
zee5|https://www.zee5.com/...|1080p|anime
```

Then run:
```bash
python scripts/run_all.py --config config/batch_list.txt --workers 2
```

---

## Output Structure

```
output/
├── movies/
│   └── Mirzapur (2018) [AmazonPrime] [1080p] [Hindi|English].mkv
├── shows/
│   └── Scam 1992 S01E01 (2020) [SonyLIV] [1080p] [Hindi].mkv
├── anime/
│   └── Demon Slayer S03E01 (2023) [Netflix] [1080p] [Japanese|English].mkv
└── documentaries/
    └── Making of India (2022) [Hotstar] [1080p] [Hindi|English].mkv
```
