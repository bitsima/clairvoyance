from fastapi import UploadFile
import redis

import hashlib
import io

from config import redis_db, redis_host, redis_port
from src.api.schemas import extracted_data


redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

extracted_data.ExtractedData.__dict__


def get_cache(file_hash: str) -> extracted_data.ExtractedData | None:
    cached_data = redis_client.hgetall(file_hash)
    if cached_data != {}:
        return cached_data
    return None


def hash_with_SHA256(file: UploadFile) -> str:
    with open(io.BytesIO(file), "rb") as file:
        data = file.read()
        sha256_returned = hashlib.sha256(data).hexdigest()
    return sha256_returned
