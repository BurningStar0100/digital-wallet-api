from typing import Optional
from pydantic import BaseModel


class UserRequest(BaseModel):
    username: Optional[str] = None
    phone_number: Optional[str] = None