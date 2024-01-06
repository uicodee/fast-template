from fastapi import FastAPI
from .test import router as test_router


def setup(app: FastAPI):
    app.include_router(
        router=test_router,
        tags=["Test"]
    )
