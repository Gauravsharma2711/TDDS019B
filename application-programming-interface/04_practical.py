from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Address(BaseModel): 
    city : str
    state : str
    pincode : int

class Order (BaseModel): #Smallest Class
    order_id :int
    order_date : str


class Customer (BaseModel):
    name : str
    cust_id : int
    phone : int
    order : Order
    address : Address

class Employee (BaseModel):
    name : str
    emp_id : int
    phone : int
    address : Address 

class Store (BaseModel) :
    customer : Customer
    employee : Employee
    address : Address

@app.post("/stores")
def create_student(store : Store):
    return{
        "message" : "Store Added Succesfully " , 
        "store" : store
    }

@app.post("/customers")
def create_student(customer : Customer):
    return{
        "message" : "Customer Added Successfully " , 
        "customer" : Customer
    }

@app.post("/employees")
def create_student(employee : Employee):
    return{
        "message" : "Employee Added Successfully " , 
        "employee" : employee
    }

@app.get("/")
def home():
    return {"message" : "Nested model API"}