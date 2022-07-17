FROM python:alpine3.15

RUN pip install kubernetes==23.3.0

COPY sync.py .

ENV WHITELIST_MIDDLEWARE_NAME=ip-whitelist
ENV WHITELIST_TRAEFIK_NAMESPACE=traefik-system

CMD ["python", "sync.py"]
