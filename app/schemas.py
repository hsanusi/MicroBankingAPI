from pydantic import BaseModel

class Customer(BaseModel):
    title: str 
    surname: str
    first_name: str
    other_names: str
    address: str
    phone_number: str
    is_active: bool=True

class Transaction(BaseModel):
    ledger_code: str
    customer_id: str
    channel: str
    trans_type: str
    trans_reference: str
    amount: float
    narration: str
    initiated_by: str
    status: int

class User(BaseModel):
    email: str
    password: str