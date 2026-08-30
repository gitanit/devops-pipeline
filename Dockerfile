FROM python:3.12-slim

WORKDIR /app

COPY application.py .

EXPOSE 8080

CMD ["python", "application.py"]
