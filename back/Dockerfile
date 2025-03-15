FROM python:3.12-slim
LABEL authors="urtanto"

COPY back/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY back/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]