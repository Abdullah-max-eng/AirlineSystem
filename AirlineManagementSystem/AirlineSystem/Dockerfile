FROM python:3
COPY .  /usr/src/app/
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]
