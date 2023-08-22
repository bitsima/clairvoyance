from fastapi import UploadFile
from PIL import Image
import pytesseract


def extract_data(file: UploadFile):
    extracted_str = pytesseract.image_to_string(Image.open(file))
    ####regex and imported validation functions
