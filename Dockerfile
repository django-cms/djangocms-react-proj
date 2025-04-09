FROM python:3.11

WORKDIR /app

RUN python -m pip install --upgrade pip

# optimizing the docker caching behaviour
COPY requirements.txt .

# Before the pip install step, add:
RUN apt-get update && apt-get install -y \
build-essential \
python3-dev \
libpq-dev \
libxml2-dev \
libxslt1-dev \
zlib1g-dev \
libcairo2-dev \
libpango1.0-dev \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# Alternatively, for psycopg2 specifically:
# Replace psycopg2 with psycopg2-binary in requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .

RUN python manage.py collectstatic --noinput

CMD uwsgi --http=0.0.0.0:80 --module=backend.wsgi
