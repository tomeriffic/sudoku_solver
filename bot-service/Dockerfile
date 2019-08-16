FROM python:3-alpine

COPY . /bot-service

WORKDIR /bot-service

RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

