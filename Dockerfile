FROM centos/python-36-centos7

COPY . /app

WORKDIR /app
RUN pip install -r requirements.txt

CMD python run.py --host=0.0.0.0