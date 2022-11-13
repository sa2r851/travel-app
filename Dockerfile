FROM python:3.10.8-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN pip install --upgrade pip --no-cache-dir
COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY ./myproject ./
EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
