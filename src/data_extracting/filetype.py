from fastapi import UploadFile
import filetype


ACCEPTED_TYPES = {"jpg", "jpeg", "png", "tiff", "webp"}  # more supported types


def is_acceptable_filetype(file: UploadFile) -> bool:
    try:
        type = filetype.guess_extension(file)
        if type not in ACCEPTED_TYPES:
            raise TypeError
        else:
            return True
    except TypeError:
        return False
