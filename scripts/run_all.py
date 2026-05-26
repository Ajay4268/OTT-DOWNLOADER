"""
run_all.py — Batch rip from a list of URLs.

Batch file format (one entry per line):
    platform|url|quality|type
    netflix|https://www.netflix.com/watch/123|1080p|movies
    jiocinema|https://www.jiocinema.com/...|4K|shows

Usage:
    python scripts/run_all.py --config config/batch_list.txt
    python scripts/run_all.py --config config/batch_list.txt --workers 3
"""
import argparse
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.downloader import download
from utils.cookies import get_cookie_path
from utils.logger import get_logger
from rich.progress import Progress, SpinnerColumn, TextColumn

logger = get_logger("run_all")


def parse_batch_file(path: str) -> list[dict]:
    tasks = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("|")
            if len(parts) < 2:
                continue
            tasks.append({
                "platform": parts[0].strip(),
                "url":      parts[1].strip(),
                "quality":  parts[2].strip() if len(parts) > 2 else "1080p",
                "type":     parts[3].strip() if len(parts) > 3 else "movies",
            })
    return tasks


def rip_task(task: dict) -> tuple[str, bool]:
    cookie_file = get_cookie_path(task["platform"])
    success = download(
        url=task["url"],
        platform=task["platform"],
        content_type=task["type"],
        quality=task["quality"],
        cookie_file=cookie_file,
    )
    return task["url"], success


def main():
    parser = argparse.ArgumentParser(description="OTT Ripper — batch mode")
    parser.add_argument("--config",  required=True, help="Batch list file path")
    parser.add_argument("--workers", type=int, default=2,
                        help="Number of parallel downloads (default: 2)")
    args = parser.parse_args()

    tasks = parse_batch_file(args.config)
    logger.info(f"Loaded {len(tasks)} tasks from {args.config}")

    results = {"success": 0, "failed": 0}

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(rip_task, t): t for t in tasks}
        for future in as_completed(futures):
            url, ok = future.result()
            if ok:
                results["success"] += 1
            else:
                results["failed"] += 1
                logger.error(f"FAILED: {url}")

    logger.info(f"Done. ✅ {results['success']} succeeded  ❌ {results['failed']} failed")


if __name__ == "__main__":
    main()
