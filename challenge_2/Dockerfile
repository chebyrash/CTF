FROM debian:stable-slim

COPY ["generate.sh", "entry.sh", "/"]

COPY ["src/*", "home/"]

RUN apt-get update \
    && apt-get install netcat zip gcc libc6-dev -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/entry.sh"]