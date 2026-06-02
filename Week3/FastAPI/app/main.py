from fastapi import FastAPI
from model import product

app = FastAPI()
@app.get('/')
def greet():
    return "hello API"

products =[
    product(id=1,name="watch",description="fossil watch",price=7000,quantity=10),
    product(id=2,name="Laptop",description="Dell Laptop",price=70000,quantity=20),
    product(id=3,name="Mobile",description="fApple",price=170000,quantity=30),
    product(id=4,name="TV",description="LG",price=37000,quantity=4)
]
@app.get('/product')
def get_all_products():
    return products

@app.get('/product/{id}')
def get_by_products(id : int ):
    for product in products:
        if product.id == id:
            return product
    return "product not find"

@app.post('/product')
def add_product(product : product):
    products.append(product)
    return product