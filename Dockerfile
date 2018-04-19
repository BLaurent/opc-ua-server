FROM resin/raspberrypi3-python:3-slim

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

RUN pip install --upgrade pip && \
      pip install pipenv && \
      addgroup --system --gid 1001 app && \
      adduser --system --disabled-password --home /app --uid 1001 --ingroup app app

RUN apt-get update && \
    apt-get -y -qq upgrade && \
    apt-get install gcc libffi-dev libssl-dev libxml2-dev libxslt-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /app/src

WORKDIR /app
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --deploy --system

COPY *.py ./src

RUN chown -R app.app /app/

USER app

CMD ["python3", "./src/app.py"]
