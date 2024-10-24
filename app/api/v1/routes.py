from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models.item import Item as ItemModel
from app.schemas.item import ItemCreate, Item

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
    db_item = ItemModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Define a route to get all items
@router.get("/items", response_model=Item)
def read_items(db: Session = Depends(get_db)):
    items = db.query(ItemModel).all()
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return items

