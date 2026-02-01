from fastapi import FastAPI

from Pydantic import Product

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello World"}

@app.post("/create-product/")
async def create_item(product: Product):
    return product