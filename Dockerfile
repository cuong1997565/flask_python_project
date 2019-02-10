FROM python:3.7
ADD . /code
WORKDIR /code

RUN pip install -r requirements.txt
#RUN apt install -y python-psycopg2

CMD ["python", "run.py"]
