from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    business_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    weight = Column(Float, nullable=True)
    product_sku = Column(String(100), nullable=True)
    is_express_shipping = Column(Boolean, default=False)