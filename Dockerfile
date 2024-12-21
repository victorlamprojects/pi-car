FROM python:3.11-alpine

RUN apk update
RUN apk add gcc
RUN apk add libc-dev

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "server.py"]

