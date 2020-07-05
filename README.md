# Squirro API

Sample FastAPI project based on Python 3.6.

## Installation

1. Create a new virtual environment and install the `requirements.txt`:
```
pip install -r requirements.txt
```

2. Create the small database in SQLITE3:
```
python create_db.py
```
3. Execute the project:
```
python app.py
```
Now you will have the API up and you can check the documentation here: `http://127.0.0.1:5000/docs`
You can create documents which will create automatically a summary with the text of the document and then you will be able to get the summary of your document.

## Tests

If you want to run the tests you will need to install the `test-requirements.txt` and execute the command (before you have to start the API):
```
pytest tests
```
