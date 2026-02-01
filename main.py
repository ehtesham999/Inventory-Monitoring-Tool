from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from Pydantic import Product
from dependencies import get_db
from models import Product as DBProduct
app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.post("/create-product/")
async def create_product(product: Product, db:Session=Depends(get_db)):
    db_product = DBProduct(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


