FROM python:3.7.2-slim

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		mysql-client default-libmysqlclient-dev \
		sqlite3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV DJANGO_VERSION 2.2.7

WORKDIR /
COPY . ./

RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install -r requirements.txt
# RUN pipenv install
ENTRYPOINT ["./entrypoint.sh"]