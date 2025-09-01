from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.db.db import create_tables
# from app.routes.user import user_router
# from app.routes.wallet import wallet_router

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_tables()

@app.get('/') #redirect to /docs
def read_root():
    return RedirectResponse(url='/docs')

# app.include_router(prefix= "/user", router = user_router)
# app.include_router(prefix= "/post", router = wallet_router)

