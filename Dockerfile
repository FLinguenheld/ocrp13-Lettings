FROM python:3

RUN mkdir -p /home/app
COPY . /home/app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./home/app/requirements.txt

EXPOSE 8000

CMD python /home/app/manage.py runserver 0.0.0.0:8000
