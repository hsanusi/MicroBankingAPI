from fastapi import FastAPI, status, HTTPException, Depends
from . import models
from .database import engine, get_db
from sqlalchemy.orm import Session
from . import schemas
import psycopg2


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome Micro Banking API"}

@app.post("/customers",status_code=status.HTTP_201_CREATED)
def create_customers(customer: schemas.Customer, db: Session = Depends(get_db)):
    new_customer = models.Customer(**customer.dict())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer) 
    return {"Message": new_customer}


@app.get("/customers")
def get_customers(db: Session = Depends(get_db)):
    customers = db.query(models.Customer).all()
    if not customers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Customer Record Found")
    return {"customers": customers}


@app.get("/customers/{id}")
def get_customers(id: int, db: Session = Depends(get_db)):
    customers = db.query(models.Customer).filter(models.Customer.customer_id==id).first()
    if not customers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Customer with the ID {id} Record Found")
    return {"customers": customers}


@app.post("/transactions",status_code=status.HTTP_201_CREATED)
def create_customers(transaction: schemas.Transaction, db: Session = Depends(get_db)):
    new_transaction = models.Transaction(**transaction.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction) 
    return {"Transaction": new_transaction}

@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).all()
    if not transactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Transaction Record Found")
    return {"Transactions": transactions}


@app.get("/transactions/{id}")
def get_transactions(id:int, db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).filter(models.Transaction.transaction_id == id).first()
    if not transactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Transaction Record Found")
    return {"Transactions": transactions}


@app.get("/customer/transactions/{id}")
def get_customer_transactions(id: int, db: Session = Depends(get_db)):
    transactions = db.query(models.Transaction).filter(models.Customer.customer_id == id).all()
    print(transactions)
    if not transactions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Transaction Record Found for Customer ID {id} ")
    return {"Customer Transactions": transactions}





@app.post("/users",status_code=status.HTTP_201_CREATED)
def create_users(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user) 
    return {"Message": new_user}