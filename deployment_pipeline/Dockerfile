FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY model_dir ./model_dir

EXPOSE 8000

CMD ["python", "app.py"]