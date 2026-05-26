"""
Standardise output filenames across all platforms.

Format: Title (Year) [Platform] [Quality] [Audio].mkv
Example: Mirzapur S02E05 (2020) [AmazonPrime] [1080p] [Hindi+English].mkv
"""
import re


def build_filename(
    title: str,
    year: str = None,
    platform: str = None,
    quality: str = "1080p",
    audio_langs: list = None,
    season: int = None,
    episode: int = None,
) -> str:
    safe_title = re.sub(r'[\\/*?:"<>|]', "", title).strip()

    ep_tag = ""
    if season and episode:
        ep_tag = f" S{season:02d}E{episode:02d}"
    elif season:
        ep_tag = f" S{season:02d}"

    year_tag = f" ({year})" if year else ""
    platform_tag = f" [{platform}]" if platform else ""
    quality_tag = f" [{quality}]"
    audio_tag = ""
    if audio_langs:
        audio_tag = f" [{'|'.join(audio_langs)}]"

    return f"{safe_title}{ep_tag}{year_tag}{platform_tag}{quality_tag}{audio_tag}.mkv"
