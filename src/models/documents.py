from pydantic import BaseModel


class Document(BaseModel):
    document_id: int
    summary: str


class NewDocument(BaseModel):
    document_id: int
