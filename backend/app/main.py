from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.routes.customer import router as customer_router

app = FastAPI(
    title="Water Refilling Station API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    customer_router,
    prefix="/api/v1"
)

@app.get("/")
def home():
    return {
        "message": "Water Refilling Station API"
    }

@app.get("/customers")
def customers():
    return {
        "status": "ok"
    }
