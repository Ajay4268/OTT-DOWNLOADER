"""
single_rip.py — Rip a single title from any supported OTT platform.

Usage:
    python scripts/single_rip.py --platform netflix --url "https://www.netflix.com/watch/XXXXX"
    python scripts/single_rip.py --platform jiocinema --url "..." --quality 4K --type movies
"""
import argparse
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.downloader import download
from utils.cookies import get_cookie_path
from utils.logger import get_logger

logger = get_logger("single_rip")

PLATFORM_MAP = {
    # Global
    "netflix":    "scripts.global.netflix",
    "prime":      "scripts.global.prime",
    "disney":     "scripts.global.disney",
    "hbomax":     "scripts.global.hbomax",
    "hulu":       "scripts.global.hulu",
    "apple":      "scripts.global.apple",
    "peacock":    "scripts.global.peacock",
    "paramount":  "scripts.global.paramount",
    # Indian
    "hotstar":    "scripts.indian.hotstar",
    "jiocinema":  "scripts.indian.jiocinema",
    "sonyliv":    "scripts.indian.sonyliv",
    "zee5":       "scripts.indian.zee5",
    "altbalaji":  "scripts.indian.altbalaji",
    "erosnow":    "scripts.indian.erosnow",
    "manoramamax":"scripts.indian.manoramamax",
    "hoichoi":    "scripts.indian.hoichoi",
    # Regional
    "aha":        "scripts.regional.aha",
    "mxplayer":   "scripts.regional.mxplayer",
    "voot":       "scripts.regional.voot",
    "shemaroo":   "scripts.regional.shemaroo",
    "sun_nxt":    "scripts.regional.sun_nxt",
    "yupp_tv":    "scripts.regional.yupp_tv",
    "stage":      "scripts.regional.stage",
}


def main():
    parser = argparse.ArgumentParser(description="OTT Ripper — single title")
    parser.add_argument("--platform", required=True, choices=list(PLATFORM_MAP.keys()),
                        help="Platform to rip from")
    parser.add_argument("--url",      required=True, help="Content URL")
    parser.add_argument("--quality",  default="1080p",
                        choices=["4K","1080p","720p","480p"], help="Output quality")
    parser.add_argument("--type",     default="movies",
                        choices=["movies","shows","anime","documentaries"],
                        help="Content type (affects output folder)")
    parser.add_argument("--subs",     action="store_true", default=True,
                        help="Download subtitles")
    parser.add_argument("--audio",    nargs="+", default=["hi","en"],
                        help="Audio language codes (e.g. hi en ta te)")
    args = parser.parse_args()

    cookie_file = get_cookie_path(args.platform)
    if not cookie_file:
        logger.warning(f"No cookie file found for '{args.platform}'. "
                       f"Place it at cookies/{args.platform}.txt")

    logger.info(f"Platform : {args.platform.upper()}")
    logger.info(f"Quality  : {args.quality}")
    logger.info(f"Type     : {args.type}")
    logger.info(f"URL      : {args.url}")

    success = download(
        url=args.url,
        platform=args.platform,
        content_type=args.type,
        quality=args.quality,
        cookie_file=cookie_file,
        subtitles=args.subs,
        audio_langs=args.audio,
    )
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
