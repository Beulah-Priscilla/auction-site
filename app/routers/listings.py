from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

@router.post("/listings/", response_model=schemas.Listing)
def create_listing(listing: schemas.ListingCreate, db: Session = Depends(database.get_db)):
  db_listing = models.Listing(**listing.model.dump())
  db.add(db_listing)
  db.commit()
  db.refresh(db_listing)
  return db_listing

