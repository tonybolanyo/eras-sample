# ---- Python base ----
FROM python:3.7.4 AS base

# ---- Dependencias del sistema
FROM base AS system-base


# Needed for ERD docs generation
RUN apt-get update && apt-get install -y graphviz libgraphviz-dev pkg-config

COPY ./docker/start.sh /start.sh
COPY ./docker/wait_for_postgres.sh /wait_for_postgres.sh
RUN chmod +x /start.sh && chmod +x /wait_for_postgres.sh && mkdir /logs

# ---- Python requirements
FROM system-base AS dependencies

RUN mkdir -p /app/requirements

COPY ./backend/requirements/base.txt /app/requirements/
COPY ./backend/requirements/dev.txt /app/requirements/
COPY ./backend/requirements/prod.txt /app/requirements/

RUN pip install --upgrade pip \
 && pip install -r /app/requirements/dev.txt

# ---- Release target
FROM system-base as release

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY --from=dependencies /root/.cache /root/.cache
COPY --from=dependencies /app/requirements/base.txt /app/requirements/
COPY --from=dependencies /app/requirements/prod.txt /app/requirements/
RUN pip install -r /app/requirements/prod.txt && rm -rf /root/.cache

COPY ./backend/src /app/
WORKDIR /app/src

# ---- Development version
FROM dependencies AS develop

COPY --from=dependencies /root/.cache /root/.cache
COPY --from=dependencies /app/requirements/base.txt /app/requirements/
COPY --from=dependencies /app/requirements/dev.txt /app/requirements/
RUN pip install -r /app/requirements/dev.txt && rm -rf /root/.cache

COPY ./docker/run_tests.sh /app/

WORKDIR /app/src
