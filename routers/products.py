from dependencies import get_db
from fastapi import APIRouter, Depends
import schemas
from crud import products as crud

router = APIRouter(prefix="/product", tags=["product"])


@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db=Depends(get_db)):
    return crud.create_product(product, db)


@router.get("/", response_model=list[schemas.ProductResponse])
def get_products(db=Depends(get_db)):
    return crud.get_products(db)


@router.get("/detail", response_model=schemas.ProductResponse)
def get_product_detail(id: int, db=Depends(get_db)):
    response = crud.product_detail(db, id)
    if not response:
        return {"message": "Product not found"}
    return response


@router.delete("/")
def delete_product(id: int, db=Depends(get_db)):
    success = crud.product_delete(db, id)
    if success:
        return {"message": "Product deleted successfully"}
    return {"message": "Product not found"}


@router.put("/", response_model=schemas.ProductResponse)
def update_product(id: int, updated_product: schemas.ProductUpdate, db=Depends(get_db)):
    response = crud.product_update(db, id, updated_product)
    if not response:
        return {"message": "Product not found"}
    return response
