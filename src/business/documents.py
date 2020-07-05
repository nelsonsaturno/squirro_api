from gensim.summarization.summarizer import summarize

from src.business.exceptions import ShortTextException, DocumentNotFound
from src.database import sqlite


def create_document(text):
    try:
        summary = summarize(text, ratio=0.1)
    except ValueError as e:
        raise ShortTextException(str(e))
    document_id = sqlite.insert_document(text, summary)
    return document_id


def get_document_summary(document_id):
    summary = sqlite.get_document_summary(document_id)
    if summary is None:
        raise DocumentNotFound("Document {} does not exist".format(document_id))
    return summary
