FROM python:3.8-alpine3.11

COPY requirements.txt .
COPY remove-dockerhub-tag.py .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "remove-dockerhub-tag.py"]
