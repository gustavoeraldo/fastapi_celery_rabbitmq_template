FROM python:3.7

COPY . /app 
COPY ./requirements.txt /app

WORKDIR /app

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get clean

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]