from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.item import ItemCreate, Item
from app.services.item_service import ItemService

# Create a new FastAPI router
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Define a route to create a new item
@router.post("/items", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return ItemService.get_all_items(item, db)


# Define a route to get all items
@router.get("/items", response_model=Item)
def read_items(db: Session = Depends(get_db)):
    items = ItemService.get_all_items(db)
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return items

