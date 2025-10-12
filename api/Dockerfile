FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py schema.py wait_for_model.py ./
EXPOSE 8000
CMD ["python", "app.py"]