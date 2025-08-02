"""utility functions"""

from pathlib import Path


def get_files_in_directory(directory: str | Path) -> list[str]:
    """gets files in directory"""
    directory = Path(directory)

    files = [str(file_path) for file_path in directory.iterdir() if file_path.is_file()]

    return files


def get_downloaded_videos() -> list[str]:
    """gets downloaded videos"""
    return get_files_in_directory("videos/")


def load_urls_from_file(filename: str) -> list[str]:
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]
