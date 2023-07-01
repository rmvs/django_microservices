FROM python:3.11

WORKDIR /todos

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT [ "gunicorn", "main:app","-w", "3" ,"-b", "0.0.0.0:8080" ]
