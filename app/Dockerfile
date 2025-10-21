# Python 3.11 tabanlı image 
FROM python:3.11-slim

# create work direction
WORKDIR /app

# Load requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# start flask app
CMD ["python", "app.py"]
