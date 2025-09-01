from datetime import datetime
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm.session import Session

from app.models.models import User
from app.schemas.user import UserRequest

def getUserProfileById(user_id:int,db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404,
                            detail= f"User with id {user_id} not found."
                            )
    else:
        return user

def updateUserProfileById(user_id:int , user_data: UserRequest, db:Session):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404,
                            detail= f"User with id {user_id} not found."
                            )
    updated = False
    if user_data.username:
        user.username = user_data.username
        user.update_at = datetime.now()
        updated = True
    if user_data.phone_number:
        user.phone_number = user_data.phone_number
        user.update_at = datetime.now()
        updated = True
    if not updated :
        raise HTTPException(status_code=220,
                            detail="Provide relevant update details")
    else:
        db.commit()
        db.refresh(user)
        return user