FROM python:3.10

RUN mkdir -p /usr/src/
WORKDIR /usr/src/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install fastapi uvicorn redis aiohttp fastapi_utils python-dotenv

COPY . /usr/src/
