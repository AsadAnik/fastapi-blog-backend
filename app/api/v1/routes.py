from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.item import ItemCreate, Item, ItemUpdate, ItemDelete
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


# Define a route to get an item by ID
@router.put('/items/{item_id}', response_modal=Item)
def update_item(item: ItemUpdate, db: Session = Depends(get_db)):
    return ItemService.update_item(item, db)


# Define a route to delete an item by ID
@router.delete('/items/{item_id}', response_model=Item)
def delete_item(item: ItemDelete, db: Session = Depends(get_db())):
    return ItemService.delete_item(item.id, db)