from fastapi import APIRouter, UploadFile, JSONResponse, BackgroundTasks

from ...data_extracting.filetype import is_acceptable_filetype

router = APIRouter()


@router.post("/upload")
async def upload_image(background_tasks: BackgroundTasks, file: UploadFile):
    if is_acceptable_filetype(file):
        pass
    # check if cached
    # process image
    return JSONResponse(content={"message": "Image uploaded successfully"})
