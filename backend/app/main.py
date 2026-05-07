from fastapi import FastAPI

app = FastAPI(title="RVSIS Auto Trader")

@app.get("/")
def health():
    return {"status": "running"}