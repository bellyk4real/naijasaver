FROM python:3.6-alpine

ENV INSTALL_PATH /naijasaver
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN pip install --editable .

CMD gunicorn -b 0.0.0.0:80000 --access-logfile - "naijasaver:create_app()"