FROM python:slim

COPY ["generate.sh", "entry.sh", "/"]

COPY ["src/*", "home/"]

RUN apt-get update \
    && apt-get install socat netcat zip -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/entry.sh"]