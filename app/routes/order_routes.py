from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Order, OrderItem, MenuItem

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/")
def create_order(db: Session = Depends(get_db)):
    new_order = Order()
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

@router.post("/{order_id}/add-item")
def add_item_to_order(order_id: int, item_id: int, quantity: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not menu_item:
        raise HTTPException(status_code=404, detail="Item do cardápio não encontrado")
    
    order_item = OrderItem(order_id=order_id, menu_item_id=item_id, quantity=quantity)
    order.total += menu_item.price * quantity
    db.add(order_item)
    db.commit()
    db.refresh(order)
    return order
