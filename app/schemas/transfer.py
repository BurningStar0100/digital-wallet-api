from pydantic import BaseModel


class TransferRequest(BaseModel):
    sender_user_id : int
    recipent_user_id : int
    amount : float
    description : str

class TransferResponse(BaseModel):
    sender_transaction_id: int
    recipient_transaction_id: int
    amount: float
    sender_new_balance: float
    recipient_new_balance: float
    