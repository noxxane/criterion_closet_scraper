"""program to scrape the criterion collection youtube playlist for movies using
yt-dlp and ocr"""

import os
import downloader
import end_frames
import ocr
import utils

if __name__ == "__main__":
    download_list = utils.load_urls_from_file("download_list.txt")
    for url in download_list:
        os.makedirs("end_frames", exist_ok=True)
        os.makedirs("ocr", exist_ok=True)

        print("Checking if video is already downloaded...")
        if downloader.is_video_downloaded(url):
            print("Video already downloaded.")
        else:
            print(f"Downloaded video {url}...")
            downloader.download_video(url)

        print(f"Done with {url}!")

    print("Creating end frames...")
    end_frames.create_end_frames()

    print("Performing OCR...")
    ocr.perform_ocr()
    print("Done!")
