FROM mongo:8.0.18-noble

RUN useradd -m -u 1001 mongoapp \
    && mkdir -p /data/db \
    && chown -R mongoapp:mongoapp /data/db

USER mongoapp