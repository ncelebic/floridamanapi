FROM python:3
ADD app/ /app
WORKDIR /app
RUN apt-get update
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
CMD python app.py
