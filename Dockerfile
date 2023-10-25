FROM python:3.11-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip 
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE 19003

CMD ["python", "manage.py", "runserver", "0.0.0.0:19003"]
