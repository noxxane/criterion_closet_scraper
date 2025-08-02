"""ocr using pytesseract"""

import os
from PIL import Image
import pytesseract
import utils


def perform_ocr():
    """performs ocr on all files in end frames"""
    end_frames_directory = "end_frames/"
    files = utils.get_files_in_directory(end_frames_directory)

    for file in files:
        films_ocr = pytesseract.image_to_string(Image.open(file))
        common_mistakes_corrected_ocr = films_ocr.replace("|", "I")
        films = list(
            filter(lambda x: x, common_mistakes_corrected_ocr.splitlines()[1:])
        )

        with open(
            "ocr/" + os.path.splitext(file)[0].split("/")[1] + ".txt",
            "w",
            encoding="utf-8",
        ) as f:
            f.write("\n".join(films))
