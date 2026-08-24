FROM python:3.12-slim

WORKDIR /app

COPY application.py .

CMD ["python", "application.py"]
