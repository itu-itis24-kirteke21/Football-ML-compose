FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY features.py trainer.py ./
COPY data ./data
# Default command can be overridden by compose
CMD ["python", "trainer.py"]