from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URI = os.getenv('SUPABASE_URI')

engine = create_engine(SUPABASE_URI, echo=True)

class Base(DeclarativeBase):
    pass


def get_session():
    with Session(engine) as session:
        yield session

def create_tables():
    from app.models.models import User, Wallet
    Base.metadata.create_all(engine)

