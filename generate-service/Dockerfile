FROM python:3-alpine

COPY . /generate-service

WORKDIR /generate-service

RUN pip install -r requirements.txt

CMD ["python", "generate.py"]

