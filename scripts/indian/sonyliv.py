"""
Sonyliv — OTT ripper script.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from utils.downloader import download
from utils.cookies import get_cookie_path

PLATFORM = "sonyliv"


def rip(url: str, quality: str = "1080p", content_type: str = "movies", **kwargs):
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
    parser = argparse.ArgumentParser(description=f"Rip from Sonyliv")
    parser.add_argument("--url",     required=True)
    parser.add_argument("--quality", default="1080p")
    parser.add_argument("--type",    default="movies")
    args = parser.parse_args()
    rip(args.url, quality=args.quality, content_type=args.type)
