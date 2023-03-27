FROM python:3.8.2-alpine3.11
RUN apk add --no-cache bash

WORKDIR /app
COPY ./server.py /app/
RUN mkdir /serverdata
RUN touch /serverdata/file.txt
EXPOSE 9000
CMD ["python", "-u", "server.py"]