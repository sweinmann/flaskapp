FROM python:3.6.9-alpine3.10

RUN mkdir -p /app
WORKDIR /app
COPY app /app

RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN apk add binutils libc-dev

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
