"""downloads videos using youtubedl"""

import logging
from yt_dlp import YoutubeDL
import utils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_video_info(url: str) -> dict:
    """gets video info using youtubedl"""
    try:
        with YoutubeDL() as ydl:
            info_dict = ydl.extract_info(url, download=False)
            return {"id": info_dict.get("id"), "title": str(info_dict.get("title"))}
    except Exception as e:
        logger.error(f"Failed to extract video info for {url}: {e}")
        raise


def is_video_downloaded(url) -> bool:
    """checks if a given video is downloaded"""
    try:
        video_info = get_video_info(url)
        video_title = video_info["title"]

        downloaded_videos = utils.get_downloaded_videos()
        return any(video_title in video for video in downloaded_videos)
    except Exception as e:
        logger.error(f"Failed to download video from {url}: {e}")
        return False


def download_video(url):
    """downloads a video using youtubedl"""
    ydl_opts = {
        "outtmpl": "videos/%(title)s [%(id)s].%(ext)s",
        "format": "best[height<=720]",
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
