from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.database import get_db
from typing import List

router = APIRouter()

@router.post("/listings/", response_model=schemas.Listing)
def create_listing(listing: schemas.ListingCreate, db: Session = Depends(get_db)):
  db_listing = models.Listing(**listing.model_dump())
  db.add(db_listing)
  db.commit()
  db.refresh(db_listing)
  return db_listing

@router.get("/listings/", response_model=List[schemas.Listing])
def get_listings(db: Session = Depends(get_db)):
  listings = db.query(models.Listing).all()
  return listings

@router.get("/listings/{listing_id}", response_model=schemas.Listing)
def get_listing(listing_id: int, db: Session = Depends(get_db)):
  listing = db.query(models.Listing).filter(models.Listing.id == listing_id).first()
  if not listing:
    raise HTTPException(status_code=404, detail="Listing not found")
  return listing
