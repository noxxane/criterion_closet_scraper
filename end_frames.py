"""extracts end frames from videos; hardcoded just because all the criterion
videos should be the same, and if they aren't, the whole pipeline is screwed and
that's the least of this program's concerns"""

import os
import cv2
import utils


def create_end_frames():
    """creates end frames by going back ten seconds in the videos"""
    videos_directory = "videos/"
    files = utils.get_files_in_directory(videos_directory)

    for file in files:
        cap = cv2.VideoCapture(file)

        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

        target_timestamp = duration - 10

        cap.set(cv2.CAP_PROP_POS_MSEC, target_timestamp * 1000)

        ret, frame = cap.read()
        if ret:
            cv2.imwrite(
                "end_frames/" + os.path.splitext(file)[0].split("/")[1] + ".png", frame
            )

        cap.release()
