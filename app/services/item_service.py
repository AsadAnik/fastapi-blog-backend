from app.db.models.item import Item as ItemModel
from app.schemas.item import ItemCreate
from sqlalchemy.orm import Session

# ItemService class to handle item-related operations
class ItemService:
    # Get all items
    @staticmethod
    def get_all_items(db: Session):
        items = db.query(ItemModel).all()
        return items

    # Create a new item
    @staticmethod
    def create_item(item: ItemCreate, db: Session):
        db_item = ItemModel(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    # Get an item by ID
    @staticmethod
    def get_item_by_id(item_id: str, db: Session):
        item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
        return item