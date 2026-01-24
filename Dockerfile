FROM python:3.11-slim

WORKDIR /app

ENV MCP_HTTP_PORT=10000

COPY requirements.txt .
RUN python -m pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

COPY main.py .

CMD ["sh", "-c", "export MCP_HTTP_PORT=$PORT && python main.py"]
