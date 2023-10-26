FROM python:3.11

WORKDIR /code

COPY ./requirements.txt .

RUN apt-get update
RUN apt-get install -y build-essential libssl-dev libffi-dev
RUN pip install --upgrade pip
RUN pip install aiohttp
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Команда для запуска Django-сервера
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
