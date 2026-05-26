"""
Logging utility with rich terminal output.
"""
import logging
from rich.logging import RichHandler
from datetime import datetime
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

def get_logger(name: str) -> logging.Logger:
    log_file = f"logs/session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[
            RichHandler(rich_tracebacks=True),
            logging.FileHandler(log_file),
        ],
    )
    return logging.getLogger(name)
