from fastapi import FastAPI
from app.routers import listings
from app import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(listings.router)
