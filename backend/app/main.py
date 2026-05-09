from fastapi import FastAPI
from app.api.signals import router as signal_router

app = FastAPI(
    title="RVSIS Auto Trader"
)

app.include_router(
    signal_router
)


@app.get("/")
def health():

    return {
        "status": "running"
    }