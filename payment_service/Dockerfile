# Basisimage
FROM python:3.10-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Dependencies installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Sourcecode kopieren
COPY . .

# Port konfigurieren (optional, rein informativ)
EXPOSE 8000

# Startbefehl für FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]