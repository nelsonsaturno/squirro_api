import sqlite3


def create_tables():
    query = """
        CREATE TABLE IF NOT EXISTS documents (
            document_id INTEGER PRIMARY KEY AUTOINCREMENT,
            body TEXT NOT NULL,
            summary TEXT
        );
    """
    with sqlite3.connect('squirro.db') as connection:
        connection.execute(query)


if __name__ == '__main__':
    create_tables()
