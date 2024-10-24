from fastapi import FastAPI
from app.api.v1.routes import router as item_router
from app.db.base import Base
from app.db.session import engine

# Initialize the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(item_router, prefix="/api/v1")