from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class TradeRequest(BaseModel):
    symbol: str
    quantity: int


@router.get("/signals")
def get_signals():

    scanner1 = [
        "TCS",
        "INFY",
        "SBIN",
        "SBIN"
    ]

    scanner2 = [
        "INFY",
        "SBIN",
        "RELIANCE"
    ]

    common = list(
        set(scanner1) & set(scanner2)
    )

    return {
        "signals": common
    }


@router.post("/run-scanners")
def run_scanners():

    return {
        "mode": "manual",
        "status": "scanner triggered"
    }


@router.post("/confirm-trade")
def confirm_trade(
    request: TradeRequest
):

    return {
        "status": "pending_kite_execution",
        "symbol": request.symbol,
        "quantity": request.quantity
    }