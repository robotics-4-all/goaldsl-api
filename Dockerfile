FROM python:3.7

RUN pip install fastapi uvicorn textx python-multipart

EXPOSE 80

COPY ./goaldsl_api /app

COPY ./third_parties/goal-dsl /goal-dsl

RUN cd /goal-dsl && pip install .

WORKDIR /app

CMD ["uvicorn", "goaldsl_api:http_api", "--host", "0.0.0.0", "--port", "80"]
