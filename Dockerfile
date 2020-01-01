FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY app/requirements.txt /code/
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add bash freetype-dev libpng-dev jpeg-dev zlib-dev lcms2-dev openjpeg-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/
