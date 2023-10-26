FROM python:3

WORKDIR /code

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Команда для запуска Django-сервера
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]