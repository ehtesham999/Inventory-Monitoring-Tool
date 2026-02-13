import schemas
from sqlalchemy.orm import Session
from models import Product as DBProduct
from utils.common_functions import generate_sku


def create_product(product: schemas.ProductCreate, db: Session):
    data = product.model_dump()
    data["product_sku"] = generate_sku(product.name)
    db_product = DBProduct(**data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_products(db: Session):
    products = db.query(DBProduct).all()
    return products


def product_detail(db: Session, id):
    product = db.query(DBProduct).get(id)
    if not product:
        return False
    return product


def product_delete(db: Session, id):
    product = db.query(DBProduct).get(id)
    if product:
        db.delete(product)
        db.commit()
        return True
    return False


def product_update(db: Session, id, updated_product: schemas.ProductUpdate):
    product = db.query(DBProduct).get(id)
    if product:
        updated_data = updated_product.model_dump(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
        return product
    return False
