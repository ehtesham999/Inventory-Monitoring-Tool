from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    business_id: int
    name: str
    description: Optional[str] = None
    weight: Optional[float] = None
    product_sku: Optional[str] = None
    is_express_shipping: Optional[bool] = False