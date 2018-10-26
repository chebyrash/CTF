FROM debian:latest

COPY ["generate.sh", "entry.sh", "/"]

COPY ["src/*", "home/"]

ENV TERM xterm-color

RUN apt-get update \
    && apt-get install socat man-db -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/entry.sh"]