from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import MenuItem

router = APIRouter(prefix="/menu", tags=["Menu"])

@router.get("/")
def list_menu(db: Session = Depends(get_db)):
    return db.query(MenuItem).all()

@router.post("/")
def add_menu_item(name: str, price: float, db: Session = Depends(get_db)):
    new_item = MenuItem(name=name, price=price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
