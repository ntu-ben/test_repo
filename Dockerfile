FROM python:3.9.2

WORKDIR /app

COPY . .
RUN pip install pytest
CMD [ "pytest" ]

CMD [ "python", "./test_math.py" ]
CMD ["tail", "-f", "/dev/null"]
