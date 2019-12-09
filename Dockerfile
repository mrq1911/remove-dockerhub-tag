FROM python:3.8.0-slim

WORKDIR /app
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD remove-dockerhub-tag.py .

ENTRYPOINT ["/usr/local/bin/python3", "/app/remove-dockerhub-tag.py"]
