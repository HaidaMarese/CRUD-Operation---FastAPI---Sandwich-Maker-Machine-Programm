from typing import List, Dict
from fastapi import HTTPException
from pydantic import BaseModel


# Create Generic CRUD Functions
class CRUD:
    @staticmethod
    def create(db: List[Dict], item: BaseModel) -> Dict:
        item_id = len(db) + 1
        item_data = {"id": item_id, **item.model_dump()}
        db.append(item_data)
        return item_data

    @staticmethod
    def read_all(db: List[Dict]) -> List[Dict]:
        return db

    @staticmethod
    def read_one(db: List[Dict], item_id: int) -> Dict:
        for item in db:
            if item["id"] == item_id:
                return item
        raise HTTPException(status_code=404, detail="Item not found")

    @staticmethod
    def update(db: List[Dict], item_id: int, updated_item: BaseModel) -> Dict:
        for item in db:
            if item["id"] == item_id:
                item.update(updated_item.model_dump())
                return item
        raise HTTPException(status_code=404, detail="Item not found")

    @staticmethod
    def delete(db: List[Dict], item_id: int) -> Dict:
        for item in db:
            if item["id"] == item_id:
                db.remove(item)
                return {"message": "Item deleted successfully"}
        raise HTTPException(status_code=404, detail="Item not found")
