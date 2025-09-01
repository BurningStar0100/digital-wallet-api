from fastapi import APIRouter , Depends
from fastapi.datastructures import Default
from sqlalchemy.orm.session import Session

from app.db.db import get_session
from app.schemas.wallet import BalanceResponse, UpdateBalanceRequest, UpdateBalanceResponse
from app.services.wallet import getUserBalanceById, updateUserBalanceCredit, updateUserBalanceDebit


wallet_router = APIRouter()

@wallet_router.get('/{user_id}/balance' , response_model=BalanceResponse)
def get_user_balance(user_id:int , db: Session = Depends(get_session)):
    return getUserBalanceById(user_id, db)

@wallet_router.post('/{user_id}/add-money',response_model=UpdateBalanceResponse)
def add_money(user_id:int, user_data: UpdateBalanceRequest, db: Session = Depends(get_session)):
    return updateUserBalanceCredit(user_id,user_data,db)

@wallet_router.post('/{user_id}/withdraw',response_model=UpdateBalanceResponse)
def withdraw_money(user_id:int, user_data: UpdateBalanceRequest, db: Session = Depends(get_session)):
    return updateUserBalanceDebit(user_id,user_data,db)