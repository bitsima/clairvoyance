from pydantic import BaseModel


class ExtractedData(BaseModel):
    content: str | None = None
    status: str | None = None
    findings: list[dict[str, str]] = []
