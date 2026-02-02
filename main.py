from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import Pydantic
from dependencies import get_db
from utils.common_functions import generate_sku
from models import Product as DBProduct
app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.post("/create-product/", response_model=Pydantic.ProductResponse)
async def create_product(product: Pydantic.ProductCreate, db:Session=Depends(get_db)):
    data = product.model_dump()
    data['product_sku'] = generate_sku(product.name)
    db_product = DBProduct(**data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products/", response_model=list[Pydantic.ProductResponse])
async def get_products(db:Session=Depends(get_db)):
    products = db.query(DBProduct).all()
    return products


