FROM python:3.8
COPY . /app
WORKDIR /app

RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt
CMD ["python","app.py"]