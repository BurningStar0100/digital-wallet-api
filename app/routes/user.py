from fastapi import APIRouter , Depends
from fastapi.datastructures import Default
from sqlalchemy.orm.session import Session

from app.db.db import get_session
from app.schemas.user import UserRequest
from app.services.user import getUserProfileById, updateUserProfileById

user_router = APIRouter()

@user_router.get('/{user_id}')
def get_user_profile(user_id:int , db: Session = Depends(get_session)):
    return getUserProfileById(user_id, db)

@user_router.put('/{user_id}')
def update_user_profile(user_id:int, user_data: UserRequest, db: Session = Depends(get_session)):
    return updateUserProfileById(user_id,user_data,db)