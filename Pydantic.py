from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    business_id: int = Field(..., gt=0)
    name: str
    description: Optional[str] = Field(None, max_length=500)
    weight: Optional[float] = Field(None, gt=0)
    product_sku: Optional[str] = None
    is_express_shipping: Optional[bool] = False