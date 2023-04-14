FROM python:3.9.2

WORKDIR /app

COPY . .

CMD [ "python", "./test_math.py" ]
CMD ["tail", "-f", "/dev/null"]
