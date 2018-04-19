FROM python:3.6-alpine3.6

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN pip install --upgrade pip && \
      pip install pipenv && \
      addgroup -S -g 1001 app && \
      adduser -S -D -h /app -u 1001 -G app app

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev libxml2-dev libxslt-dev

RUN set -ex && mkdir /app/src

WORKDIR /app
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN set -ex && pipenv install --deploy --system

COPY *.py ./src

RUN chown -R app.app /app/

USER app

CMD ["python3", "./src/app.py"]
