from datetime import datetime
from typing import List
from typing import Optional
from sqlalchemy import TIMESTAMP, DateTime, ForeignKey, func
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.db.db import Base
from app.routes import user

class User(Base):
    __tablename__ = "user_profile"

    id: Mapped[int] = mapped_column(primary_key=True) #id SERIAL PRIMARY KEY,
    username: Mapped[str] = mapped_column(String(50),unique=True) #username VARCHAR(50) UNIQUE NOT NULL,
    email: Mapped[str] = mapped_column(String(100),unique=True) # email VARCHAR(100) UNIQUE NOT NULL,
    password: Mapped[str] = mapped_column(String(255)) #password VARCHAR(255) NOT NULL,
    phone_number: Mapped[Optional[str]] = mapped_column(String(15),nullable=True) #phone_number VARCHAR(15),
    balance: Mapped[float] = mapped_column(insert_default=0.00) # balance DECIMAL(10,2) DEFAULT 0.00,
    created_at = mapped_column(DateTime(),server_default=func.now()) # created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_at = mapped_column(DateTime(),server_default=func.now()) # update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    

class Wallet(Base):
    __tablename__ = "wallet"

    id: Mapped[int] = mapped_column(primary_key=True) #id SERIAL PRIMARY KEY,
    user_id: Mapped[int] = mapped_column(ForeignKey("user_profile.id", ondelete="CASCADE")) #user_id INTEGER REFERENCES user_profile(id) ON DELETE CASCADE,
    transaction_type: Mapped[str] = mapped_column(String(50)) #transaction_type VARCHAR(50) NOT NULL,
    amount: Mapped[float] #amount DECIMAL(10,2) NOT NULL,
    description: Mapped[str]
    created_at = mapped_column(DateTime(),server_default=func.now()) # created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    reference_transaction_id: Mapped[int] = mapped_column(ForeignKey("wallet.id", ondelete="SET NULL"), nullable=True) #reference_transaction_id INTEGER REFERENCES wallet(id) ON DELETE SET NULL,
    reference_user_id: Mapped[int] = mapped_column(ForeignKey("user_profile.id", ondelete="SET NULL"), nullable=True) #reference_user_id INTEGER REFERENCES user_profile(id) ON DELETE SET NULL,
    