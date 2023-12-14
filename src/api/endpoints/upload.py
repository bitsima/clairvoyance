from fastapi import APIRouter, UploadFile, BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi import HTTPException

from ...data_extracting.extractor import extract_data

router = APIRouter()


@router.post("/upload/")
async def upload_image(file: UploadFile):
    contents = await file.read()
    extracted_data = extract_data(contents)

    if extracted_data.status == "successful":
        return JSONResponse(extracted_data.__dict__, status_code=200)
    elif extracted_data.status == "No content found.":
        raise HTTPException(status_code=204)
    else:
        return JSONResponse(extracted_data.__dict__, status_code=400)

    # check if cached
