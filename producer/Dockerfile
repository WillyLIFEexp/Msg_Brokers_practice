FROM python:3.8-slim
WORKDIR /app
COPY /requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY ./producer /app
CMD ["python", "producer.py"]
