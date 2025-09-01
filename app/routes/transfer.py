from fastapi import APIRouter , Depends
from fastapi.datastructures import Default
from sqlalchemy.orm.session import Session
from app.db.db import get_session
from app.schemas.transfer import TransferRequest, TransferResponse
from app.services.transaction import getTransactionById
from app.services.transfer import createTransferById


transfer_router = APIRouter()

@transfer_router.post('/' , response_model= TransferResponse)
def make_a_transfer(transfer_data : TransferRequest, db: Session = Depends(get_session)):
    return createTransferById(transfer_data, db)