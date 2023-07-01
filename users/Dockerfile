FROM python:3.11

WORKDIR /users

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8081

ENTRYPOINT [ "gunicorn", "users.wsgi","-w", "3" ,"-b", "0.0.0.0:8081" ]