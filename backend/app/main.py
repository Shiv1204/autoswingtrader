from fastapi import FastAPI
from .api.signals import router as signal_router

app = FastAPI()

app.include_router(signal_router)