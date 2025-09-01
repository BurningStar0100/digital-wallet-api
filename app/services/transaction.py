from datetime import datetime
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from app.models.models import Wallet


def getTransactionById(transaction_id:int,db:Session):
    transaction = db.query(Wallet).filter(Wallet.id == transaction_id).first()
    if transaction is None:
        raise HTTPException(status_code=404,
                            detail= f"Transaction with id {transaction_id} not found."
                            )
    else:
        return transaction