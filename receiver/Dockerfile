FROM python:3.11-slim

ARG PIP_EXTRA_INDEX_URL
ARG PIP_INDEX_URL
ARG VERSION=development

ENV LOGLEVEL=info
ENV WEB_THREADS=8

COPY ./ /usr/src/
WORKDIR /usr/src/

RUN pip install pika

CMD ["python3", "receiver.py"]

