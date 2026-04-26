FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt
COPY app.py schema.py wait_for_model.py fetcher.py team_stats.py ./
COPY templates ./templates
EXPOSE 8000
CMD ["python", "app.py"]