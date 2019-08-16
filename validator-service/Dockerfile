FROM python:3-alpine

COPY . /validator-service

WORKDIR /validator-service

RUN pip install -r requirements.txt

CMD ["python", "validate.py"]

