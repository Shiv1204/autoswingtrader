from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TradeRequest(BaseModel):
    symbol: str
    quantity: int

@router.post("/run-scanners")
def run_scanners():
    return {
        "mode": "manual",
        "status": "scanner triggered"
    }

@router.post("/confirm-trade")
def confirm_trade(request: TradeRequest):
    # hook Zerodha Kite here
    return {
        "status": "pending_kite_execution",
        "symbol": request.symbol,
        "quantity": request.quantity
    }
