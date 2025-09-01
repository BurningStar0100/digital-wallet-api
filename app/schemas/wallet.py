from pydantic import BaseModel
from typing import Any

class BalanceResponse(BaseModel):
    user_id : int
    balance : float
    last_updated : Any

class UpdateBalanceRequest(BaseModel):
    amount : float
    description: str

class UpdateBalanceResponse(BaseModel):
    transaction_id : int
    user_id : int
    amount : float
    new_balance : float
    transaction_type : str

