from fastapi import FastAPI
from connection import DB

app = FastAPI(
    title="API Tennis",
    description="Microsoft AI by Simplon - AWS Infrastructure Cloud",
    version="1.0"
)

@app.get("/", tags=['Home'])
def home():
    return {"Bienvenue sur l'API":"Check les docs pour plus de fun"}

@app.get("/api/v1/members", tags=['People'])
def get_members():
    return DB.get_members()

@app.get("/api/v1/member", tags=['People'])
def get_member_by_name(name):
    return DB.get_member_by_name(name)

@app.get("/api/v1/facilities", tags=['Infrastructure'])
def get_facilities():
    return DB.get_facilities()

@app.get("/api/v1/bookings", tags=['Booking'])
def get_bookings():
    return DB.get_bookings()