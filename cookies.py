"""
Cookie management for authenticated OTT platforms.
Load cookies from browser export files (Netscape format) or environment variables.
"""
import os
from pathlib import Path


COOKIE_DIR = Path("cookies")


def get_cookie_path(platform: str) -> str | None:
    """Return path to cookie file for a platform, or None if not found."""
    path = COOKIE_DIR / f"{platform}.txt"
    if path.exists():
        return str(path)
    env_key = f"COOKIE_{platform.upper()}"
    env_val = os.environ.get(env_key)
    if env_val:
        return env_val
    return None


def list_available_cookies() -> list[str]:
    """Return list of platforms for which cookie files exist."""
    if not COOKIE_DIR.exists():
        return []
    return [f.stem for f in COOKIE_DIR.glob("*.txt")]
