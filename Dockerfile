FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Эта строчка говорит Railway, что внутри контейнера слушается порт 8080
EXPOSE 8080

COPY . .

# uvicorn будет брать порт из переменной $PORT (Railway задаёт её автоматически),
# но если вдруг по-умолчанию не передали — 8000
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
