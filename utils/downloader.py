"""
Core download engine — wraps yt-dlp with platform-specific options.
"""
import subprocess
import os
from pathlib import Path
from utils.logger import get_logger
from utils.naming_convention import build_filename

logger = get_logger(__name__)


def download(
    url: str,
    platform: str,
    content_type: str = "movies",
    quality: str = "1080p",
    cookie_file: str = None,
    output_dir: str = None,
    subtitles: bool = True,
    audio_langs: list = None,
):
    """
    Download a single title from any OTT platform via yt-dlp.

    Args:
        url:          Direct stream or page URL
        platform:     Platform identifier (e.g. 'netflix', 'jiocinema')
        content_type: 'movies' | 'shows' | 'anime' | 'documentaries'
        quality:      '4K' | '1080p' | '720p' | '480p'
        cookie_file:  Path to Netscape cookies.txt for authenticated platforms
        output_dir:   Override default output directory
        subtitles:    Download subtitles if available
        audio_langs:  List of audio language codes to download (e.g. ['hi','en'])
    """
    audio_langs = audio_langs or ["hi", "en"]
    height = _quality_to_height(quality)
    out_dir = output_dir or os.path.join("output", content_type)
    Path(out_dir).mkdir(parents=True, exist_ok=True)

    cmd = [
        "yt-dlp",
        "--format", f"bestvideo[height<={height}]+bestaudio/best[height<={height}]",
        "--merge-output-format", "mkv",
        "--output", os.path.join(out_dir, "%(title)s.%(ext)s"),
        "--audio-multistreams",
        "--no-warnings",
        "--progress",
    ]

    if cookie_file and os.path.exists(cookie_file):
        cmd += ["--cookies", cookie_file]

    if subtitles:
        cmd += [
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs", "all",
            "--convert-subs", "srt",
        ]

    for lang in audio_langs:
        cmd += ["--audio-language", lang]

    cmd.append(url)

    logger.info(f"[{platform.upper()}] Starting download → {url}")
    try:
        result = subprocess.run(cmd, check=True, text=True)
        logger.info(f"[{platform.upper()}] Download complete.")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"[{platform.upper()}] Download failed: {e}")
        return False


def _quality_to_height(quality: str) -> int:
    mapping = {"4K": 2160, "1080p": 1080, "720p": 720, "480p": 480}
    return mapping.get(quality.upper(), 1080)
