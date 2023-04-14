FROM python:3.9.2

WORKDIR /app

COPY . .

CMD [ "python", "./app.py" ]

