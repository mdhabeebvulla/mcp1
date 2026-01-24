FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

COPY main.py .

# Render sets PORT — default to 10000 if not present
CMD ["sh", "-c", "python main.py"]
