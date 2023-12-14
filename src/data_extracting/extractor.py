from fastapi import UploadFile
from PIL import Image
import pytesseract

import io
import re
from typing import Callable

from ..api.schemas.extracted_data import ExtractedData
from . import validator
from enums.data_type import DataTypes


validator_mapping: dict[DataTypes, Callable[[str], bool]] = {
    DataTypes.PHONE_NUMBER: validator.is_valid_phone_number,
    DataTypes.ID_NUMBER: validator.is_valid_id_number,
    DataTypes.CREDIT_CARD_NUMBER: validator.is_valid_cc_number,
    DataTypes.PLATE: validator.is_valid_plate_id,
    DataTypes.EMAIL: validator.is_valid_email,
    DataTypes.DOMAIN: validator.is_valid_domain,
    DataTypes.URL: validator.is_valid_url,
}


def extract_data(file: UploadFile) -> ExtractedData:
    # create the schema object
    extracted_data = ExtractedData()

    # check if the file format is one of the allowed types
    try:
        content = pytesseract.image_to_string(Image.open(io.BytesIO(file)))
    except Exception:
        extracted_data.status = "Bad request. Wrong file format."
        return extracted_data

    # verify whether there is any text present to be read in the image
    extracted_data.content = content.strip()
    if content == "":
        extracted_data.status = "No content found."
        return extracted_data

    for type_ in DataTypes:
        if type_ in validator_mapping.keys():
            needs_validation = True
        else:
            needs_validation = False

        matches = [
            match
            for pattern in type_.value
            for match in re.findall(pattern, content, re.MULTILINE)
        ]

        for match in matches:
            if not needs_validation or (
                needs_validation and validator_mapping[type_](match)
            ):
                extracted_data.findings.append({"value": match, "type": type_.name})

    extracted_data.status = "successful"
    return extracted_data
