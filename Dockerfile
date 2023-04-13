FROM python:3.9.2

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]

