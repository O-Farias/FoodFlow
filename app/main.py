from app.database import Base, engine, SessionLocal
from app.models import MenuItem, Order, OrderItem

# Inicializa o banco de dados
Base.metadata.create_all(bind=engine)

def clear_console():
    """Limpa o terminal."""
    import os
    os.system("cls" if os.name == "nt" else "clear")

def list_menu(db):
    """Lista todos os itens do cardápio."""
    items = db.query(MenuItem).all()
    if not items:
        print("O cardápio está vazio.")
    else:
        print("\nCardápio:")
        for item in items:
            print(f"- ID: {item.id} | {item.name} - R$ {item.price:.2f}")

def add_menu_item(db):
    """Adiciona um item ao cardápio."""
    name = input("Nome do item: ").strip()
    price = float(input("Preço do item: "))
    new_item = MenuItem(name=name, price=price)
    db.add(new_item)
    db.commit()
    print(f"\nItem '{name}' adicionado ao cardápio.")

def create_order(db):
    """Cria um novo pedido."""
    new_order = Order()
    db.add(new_order)
    db.commit()
    print(f"\nPedido criado com sucesso! ID do pedido: {new_order.id}")
    return new_order.id

def add_item_to_order(db):
    """Adiciona itens a um pedido existente."""
    order_id = int(input("ID do pedido: "))
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        print("Pedido não encontrado.")
        return

    list_menu(db)
    item_id = int(input("ID do item a adicionar: "))
    quantity = int(input("Quantidade: "))

    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not menu_item:
        print("Item do cardápio não encontrado.")
        return

    order_item = OrderItem(order_id=order_id, menu_item_id=item_id, quantity=quantity)
    order.total += menu_item.price * quantity
    db.add(order_item)
    db.commit()
    print(f"\n{quantity}x '{menu_item.name}' adicionado ao pedido {order_id}.")

def view_order(db):
    """Exibe detalhes de um pedido."""
    order_id = int(input("ID do pedido: "))
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        print("Pedido não encontrado.")
        return

    print(f"\nPedido #{order.id}")
    print(f"Status: {order.status}")
    print(f"Total: R$ {order.total:.2f}")
    print("Itens:")
    for item in order.items:
        menu_item = db.query(MenuItem).filter(MenuItem.id == item.menu_item_id).first()
        print(f"- {menu_item.name} (x{item.quantity})")

def update_order_status(db):
    """Atualiza o status de um pedido."""
    order_id = int(input("ID do pedido: "))
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        print("Pedido não encontrado.")
        return

    print("\nStatus disponíveis:")
    print("1. Novo")
    print("2. Preparando")
    print("3. Concluído")
    status = input("Escolha o novo status (1/2/3): ")
    status_map = {"1": "Novo", "2": "Preparando", "3": "Concluído"}
    order.status = status_map.get(status, order.status)
    db.commit()
    print(f"\nStatus do pedido {order_id} atualizado para '{order.status}'.")

def main():
    """Menu principal."""
    db = SessionLocal()
    while True:
        clear_console()
        print("🍴 Bem-vindo ao FoodFlow 🍴")
        print("1. Listar cardápio")
        print("2. Adicionar item ao cardápio")
        print("3. Criar pedido")
        print("4. Adicionar item ao pedido")
        print("5. Visualizar pedido")
        print("6. Atualizar status do pedido")
        print("7. Sair")
        print("=" * 30)

        option = input("Escolha uma opção: ").strip()

        if option == "1":
            list_menu(db)
        elif option == "2":
            add_menu_item(db)
        elif option == "3":
            create_order(db)
        elif option == "4":
            add_item_to_order(db)
        elif option == "5":
            view_order(db)
        elif option == "6":
            update_order_status(db)
        elif option == "7":
            print("\nObrigado por usar o FoodFlow! Até a próxima. 🍽️")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
