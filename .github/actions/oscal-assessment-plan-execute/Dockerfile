FROM python:3.10-alpine
COPY run.sh /run.sh
COPY requirements.txt /requirements.txt
COPY oscal.py /oscal.py
RUN pip install -r requirements.txt
ENTRYPOINT ["/run.sh"]
