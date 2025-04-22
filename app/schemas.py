from pydantic import BaseModel

class ListingCreate(BaseModel):
  title: str
  description: str
  starting_price: float

class Listing(ListingCreate):
  id: int

  class Config:
    orm_mode = True