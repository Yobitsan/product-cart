from fastapi import FastAPI,Depends
from models import Product
from fastapi.middleware.cors import CORSMiddleware
from config import SessionLocal,engine
from sqlalchemy.orm import Session
import dbmodels
app=FastAPI()
app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:3000"],allow_methods=["*"])

dbmodels.Base.metadata.create_all(bind=engine)
@app.get("/")
def greet():
    return("hi there nigger")
products=[
    Product(id=1,name="Phone",description="a smartphone",price=700.02,quantity=50),
    Product(id=5,name="Phone",description="a laptop",price=1100.02,quantity=50),
    Product(id=7,name="Phone",description="a nigga",price=100.02,quantity=50),
]
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
def init_db():
    db=SessionLocal()
    count=db.query(dbmodels.Product).count
    if count==0:
        for product in products:
            db.add(dbmodels.Product(**product.model_dump()))
    db.commit()
init_db()
@app.get("/products")
def get_all_products(db: Session=Depends(get_db)):
    db_products = db.query(dbmodels.Product).all()
    return db_products
@app.get("/products/{id}")
def get_product_by_id(id: int,db: Session=Depends(get_db)):
    output = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if output:
        return output


@app.post("/products")
def add_product(product: Product,db: Session = Depends(get_db)):
    db.add(dbmodels.Product(**product.model_dump()))
    db.commit()
    return product
@app.put("/products/{id}")
def change_product(id: int, newproduct: Product,db: Session = Depends(get_db)):
    oldprod=db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    if (oldprod):
        oldprod.name=newproduct.name
        oldprod.description = newproduct.description
        oldprod.quantity = newproduct.quantity
        oldprod.price = newproduct.price
        oldprod.id = newproduct.id
        db.commit()
        return newproduct
@app.delete("/products/{id}")
def delete_product(id: int,db: Session = Depends(get_db)):
    oldprod = db.query(dbmodels.Product).filter(dbmodels.Product.id == id).first()
    db.delete(oldprod)
    db.commit()
    

