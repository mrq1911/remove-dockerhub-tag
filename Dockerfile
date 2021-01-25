FROM alpine:3.11

COPY requirements.txt .
COPY remove-dockerhub-tag.py .

RUN apk add --no-cache python3 py3-pip && \
    pip3 install -r requirements.txt && \
    apk del --purge py3-pip && \
    rm -rf /var/cache/apk/* /tmp/*

ENTRYPOINT ["python3", "remove-dockerhub-tag.py"]
