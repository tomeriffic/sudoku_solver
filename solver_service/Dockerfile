FROM python:3-alpine

COPY . /solver_service

WORKDIR /solver_service

RUN pip install -r requirements.txt

CMD ["python", "solver.py"]

