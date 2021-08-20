FROM python:3.7

ENV PYTHONUNBUFFERED 1
WORKDIR /dashboard

COPY . .

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]