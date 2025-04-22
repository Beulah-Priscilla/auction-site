from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Listing(Base):
  __tablename__ = "listings"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  description = Column(String)
  starting_bid = Column(Float)