FROM python:3.8-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install --upgrade pip --no-cache-dir
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY ./myproject ./
EXPOSE 8000
#CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
CMD [ "gunicorn","project.wsgi:application","--bind","0.0.0.0:8000"]
