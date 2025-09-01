from fastapi import APIRouter , Depends
from fastapi.datastructures import Default
from sqlalchemy.orm.session import Session
from app.db.db import get_session
from app.services.transaction import getTransactionById


transaction_router = APIRouter()

@transaction_router.get('/{transaction_id}')
def get_user_profile(transaction_id:int , db: Session = Depends(get_session)):
    return getTransactionById(transaction_id, db)