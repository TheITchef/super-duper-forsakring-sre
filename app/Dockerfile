FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY pyproject.toml .
COPY src/ ./src/

RUN pip install -e .

EXPOSE 8000

CMD ["uvicorn", "policy_api.main:app", "--host", "0.0.0.0", "--port", "8000"]