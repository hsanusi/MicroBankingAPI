from email.policy import default
from enum import unique
from tokenize import String
from .database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, Float
from sqlalchemy.sql.expression import null,text

class Customer(Base):
    __tablename__ = "customers"
    
    customer_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    other_names = Column(String)
    address= Column(String)
    phone_number = Column(String)
    is_active = Column(Boolean, server_default='TRUE',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Transaction(Base):
    __tablename__ ="transactions"

    transaction_id = Column(Integer, primary_key=True, nullable=False)
    customer_id = Column(Integer,  nullable=False)
    ledger_code = Column(String, nullable=False)
    channel = Column(String, nullable=False)
    trans_type = Column(String, nullable=False)
    trans_reference = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    narration = Column(String, nullable=False)
    initiated_by = Column(String, nullable=False)
    status = Column(Integer,  nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))