FROM python:3.10-alpine
COPY run.sh /run.sh
COPY requirements.txt /requirements.txt
COPY app_test.py /app_test.py
RUN pip install -r requirements.txt
ENTRYPOINT ["/run.sh"]
