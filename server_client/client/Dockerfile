FROM python:3.8.2-alpine3.11
RUN apk add --no-cache bash

WORKDIR /app
COPY ./client.py /app/
RUN mkdir /clientdata
RUN touch /clientdata/file.txt
EXPOSE 9000
CMD ["python", "-u", "client.py"]