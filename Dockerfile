FROM python:3.8-slim-buster

WORKDIR /app

RUN apt update && apt install ssh -y

# key pair must be mounted as a volume into /app/.ssh directory
RUN mkdir .ssh

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "-m" , "flask", "--app", "main", "run"]
