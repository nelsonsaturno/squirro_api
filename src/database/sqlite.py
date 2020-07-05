import sqlite3

from src import settings as st


def insert_document(text, summary):
    query = """
        INSERT INTO documents (body, summary)
        VALUES (?, ?)
    """
    params = (text, summary)
    with sqlite3.connect(st.SQLITE_DB) as connection:
        cursor = connection.execute(query, params)
        document_id = cursor.lastrowid
    return document_id


def get_document_summary(document_id):
    query = """
        SELECT summary
        FROM documents
        WHERE document_id = ?
    """
    params = (document_id,)
    with sqlite3.connect(st.SQLITE_DB) as connection:
        summary = connection.execute(query, params).fetchone()
    return summary[0] if summary else None
