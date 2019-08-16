FROM python:3-alpine

COPY . /solver-service

WORKDIR /solver-service

RUN pip install -r requirements.txt

CMD ["python", "solver.py"]

