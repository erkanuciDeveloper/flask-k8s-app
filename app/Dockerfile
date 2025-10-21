FROM python:3.11-slim

WORKDIR /app

# Sistem paketleri ve sertifikalar
RUN apt-get update && apt-get install -y build-essential ca-certificates

COPY requirements.txt .

# pip upgrade ve requirements yükle
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
