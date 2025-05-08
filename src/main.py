# pylint: disable=wrong-import-position

"""
Main module for the application
"""
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import uvicorn

from src.setup import config


app = FastAPI(title=config.API_TITLE)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.API_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# fmt: off

from src.routers.resources import router as resources_router
app.include_router(resources_router, prefix="/v1/resources", tags=["RESOURCES"])

from src.routers.clients import router as clients_router
app.include_router(clients_router, prefix="/v1/clients", tags=["CLIENTS"])

# fmt: on

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host=config.API_HOST,
        port=config.API_PORT,
    )
