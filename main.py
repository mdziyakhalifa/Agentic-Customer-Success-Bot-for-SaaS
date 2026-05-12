from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

from database.database import init_db
from api import auth_routes, chat_routes, admin_routes

app = FastAPI(title="Agentic AI Customer Success Platform API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Database
@app.on_event("startup")
def on_startup():
    init_db()

# Include Routers
app.include_router(auth_routes.router)
app.include_router(chat_routes.router)
app.include_router(admin_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Agentic AI Customer Success Platform API"}
