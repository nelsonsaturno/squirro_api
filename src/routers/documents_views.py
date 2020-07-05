from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import ORJSONResponse

from src.business.exceptions import ShortTextException, DocumentNotFound
from src.models.documents import Document, NewDocument
from src.business import documents as business_documents

api_router = APIRouter(default_response_class=ORJSONResponse)


@api_router.get("/{document_id}/summary/", response_model=Document)
async def get_document(document_id: int):
    """
    Get document summary
    """
    try:
        summary = business_documents.get_document_summary(document_id)
    except DocumentNotFound as e:
        raise HTTPException(status_code=404, detail={"document_id": str(e)})
    return Document(document_id=document_id, summary=summary)


@api_router.post("/", response_model=NewDocument)
async def create_document(text: str = Form(...)):
    """
    Create document
    """
    try:
        document_id = business_documents.create_document(text)
    except ShortTextException as e:
        raise HTTPException(status_code=422, detail={"text": str(e)})
    return NewDocument(document_id=document_id)
