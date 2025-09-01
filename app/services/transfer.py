from datetime import datetime
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from app.models.models import User, Wallet
from app.schemas.transfer import TransferRequest
  
def createTransferById(transfer_data: TransferRequest, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404,
                            detail= f"User with id {user_id} not found."
                            )
    else:
        user.balance = user.balance + user_data.amount
        user.update_at = datetime.now()
        db.commit()
        db.refresh(user)
        transaction = Wallet(
            user_id = user_id,
            transaction_type = "CREDIT",
            amount = user_data.amount,
            description = user_data.description,
            created_at = datetime.now()
        )
        db.add(transaction)
        db.commit()
        db.refresh(transaction)
        data = UpdateBalanceResponse(
            transaction_id= transaction.id,
            user_id = user_id,
            amount = user_data.amount,
            new_balance= user.balance,
            transaction_type= transaction.transaction_type
        )
        return data