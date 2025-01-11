FROM python:3.13
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
