from sqlalchemy.orm import Session
from . import models, schemas

def create_listing(db: Session, listing: schemas.ListingCreate):

  db_listing = models.Listing(**listing.model_dump())
  db.add(db_listing)
  db.commit()
  db.refresh(db_listing)
  return db_listing

def get_listings(db: Session, skip: int = 0, limit: int = 10):
  return db.query(models.Listing).offset(skip).limit(limit).all()