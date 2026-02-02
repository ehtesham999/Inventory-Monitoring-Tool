from typing import Optional
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    business_id: int = Field(..., gt=0)
    name: str
    description: Optional[str] = Field(None, max_length=500)
    weight: Optional[float] = Field(None, gt=0)
    is_express_shipping: Optional[bool] = False

class ProductResponse(ProductCreate):
    id: int
    product_sku: str    
    class Config:
        from_attributes = True