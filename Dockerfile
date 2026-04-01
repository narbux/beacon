FROM ghcr.io/astral-sh/uv:alpine3.23

RUN apk --no-cache add curl

ENV UV_NO_DEV=1

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

COPY . .

EXPOSE 8080

CMD [ "uv", "run", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "--workers", "1", "beacon:app"]
