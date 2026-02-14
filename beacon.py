import logging

from fastapi import FastAPI, HTTPException, Request, status

logging.basicConfig(
    format="%(asctime)s %(levelname)-8s %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %X",
)
logger = logging.getLogger(__name__)

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.post("/beacon")
async def beacon(request: Request):
    client = request.client
    if not client:
        raise HTTPException(status.HTTP_400_BAD_REQUEST)
    logger.info(f"host: {client.host} | port: {client.port}")
    return {"ok": client.host}


@app.get("/health")
async def healthcheck():
    return {"status": "ok"}
