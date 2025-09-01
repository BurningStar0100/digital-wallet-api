from datetime import datetime
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from app.models.models import User, Wallet
from app.schemas.transfer import TransferRequest, TransferResponse
  
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
            db.refresh(sender_user)
            recipent_user.balance = recipent_user.balance + transfer_data.amount
            recipent_user.update_at = datetime.now()
            db.commit()
            db.refresh(recipent_user)
            transaction_sender = Wallet(
                user_id = transfer_data.sender_user_id,
                transaction_type = "TRANSFER_OUT",
                amount = transfer_data.amount,
                description = transfer_data.description,
                created_at = datetime.now(),
                reference_user_id = transfer_data.recipent_user_id

            )
            db.add(transaction_sender)
            db.commit()
            db.refresh(transaction_sender)
             # Create recipient transaction record
            transaction_recipient = Wallet(
                user_id=transfer_data.recipent_user_id,
                transaction_type="TRANSFER_IN",
                amount=transfer_data.amount,
                description=transfer_data.description,
                created_at=datetime.now(),
                reference_user_id=transfer_data.sender_user_id
            )
            db.add(transaction_recipient)
            db.commit()
            db.refresh(transaction_recipient)
            data = TransferResponse(
                    
                    sender_transaction_id=transaction_sender.id,
                    recipient_transaction_id=transaction_recipient.id,
                    amount=transfer_data.amount,
                    sender_new_balance=sender_user.balance,
                    recipient_new_balance=recipient_user.balance
                )
            return data
        else:
            raise HTTPException(status_code=400,
                                detail=f"Insufficient balance of {sender_user.balance} required amount {transfer_data.amount - sender_user.balance}")