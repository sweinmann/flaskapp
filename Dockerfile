FROM python:3.6.9-alpine3.10

RUN mkdir -p /app
WORKDIR /app
COPY app /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
