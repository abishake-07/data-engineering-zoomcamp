FROM python:3.13-slim 
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /pipeline
ENV PATH="/pipeline/.venv/bin:$PATH"
COPY pyproject.toml uv.lock ./
COPY ingest_data.py .
RUN uv sync --frozen


ENTRYPOINT [ "python", "ingest_data.py" ]  