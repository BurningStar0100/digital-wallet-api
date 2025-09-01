from datetime import datetime
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from app.models.models import User, Wallet
from app.schemas.transfer import TransferRequest
  
def createTransferById(transfer_data: TransferRequest, db: Session):
    sender_user = db.query(User).filter(User.id == transfer_data.sender_user_id).first()
    recipent_user = db.query(User).filter(User.id == transfer_data.recipent_user_id).first()
    if (sender_user is None) or (recipent_user is None):
        raise HTTPException(status_code=404,
                            detail= f"Users not found."
                            )
    else:
        if sender_user.balance >= transfer_data.amount:
            sender_user.balance = sender_user.balance - transfer_data.amount
            sender_user.update_at = datetime.now()
            db.commit()
            db.refresh(user)
            transaction = Wallet(
                user_id = user_id,
                transaction_type = "DEBIT",
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
        else:
            raise HTTPException(status_code=400,
                                detail=f"Insufficient balance of {user.balance}")