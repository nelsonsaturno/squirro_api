FROM python:3.6-slim

WORKDIR /

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt --upgrade

COPY . .

RUN python create_db.py

CMD ["uvicorn", "src:app", "--host", "0.0.0.0", "--port", "5000"]
