from app.database import Base, engine, SessionLocal
from app.models import MenuItem, Order, OrderItem
from colorama import Fore, Style
import os

# Inicializa o banco de dados
Base.metadata.create_all(bind=engine)

def clear_console():
    """Limpa o terminal."""
    os.system("cls" if os.name == "nt" else "clear")

def print_title(title):
    """Exibe um título com destaque."""
    print(Fore.CYAN + "=" * 30)
    print(f"{title.center(30)}")
    print("=" * 30 + Style.RESET_ALL)

def list_menu(db):
    """Lista todos os itens do cardápio."""
    items = db.query(MenuItem).all()
    print_title("Cardápio")
    if not items:
        print(Fore.YELLOW + "O cardápio está vazio." + Style.RESET_ALL)
    else:
        for item in items:
            print(f"- ID: {item.id} | {item.name} - R$ {item.price:.2f}")

def add_menu_item(db):
    """Adiciona um item ao cardápio."""
    print_title("Adicionar Item")
    name = input("Nome do item: ").strip()
    price = float(input("Preço do item: "))
    new_item = MenuItem(name=name, price=price)
    db.add(new_item)
    db.commit()
    print(Fore.GREEN + f"\n✅ Item '{name}' adicionado ao cardápio." + Style.RESET_ALL)

def create_order(db):
    """Cria um novo pedido."""
    new_order = Order()
    db.add(new_order)
    db.commit()
    print(Fore.GREEN + f"\n✅ Pedido criado com sucesso! ID do pedido: {new_order.id}" + Style.RESET_ALL)
    return new_order.id

def add_item_to_order(db):
    """Adiciona itens a um pedido existente."""
    print_title("Adicionar Item ao Pedido")
    order_id = int(input("ID do pedido: "))
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        print(Fore.RED + "❌ Pedido não encontrado." + Style.RESET_ALL)
        return

    list_menu(db)
    item_id = int(input("\nID do item a adicionar: "))
    quantity = int(input("Quantidade: "))

    menu_item = db.query(MenuItem).filter(MenuItem.id == item_id).first()
    if not menu_item:
        print(Fore.RED + "❌ Item do cardápio não encontrado." + Style.RESET_ALL)
        return

    order_item = OrderItem(order_id=order_id, menu_item_id=item_id, quantity=quantity)
    order.total += menu_item.price * quantity
    db.add(order_item)
    db.commit()
    print(Fore.GREEN + f"\n✅ {quantity}x '{menu_item.name}' adicionado ao pedido {order_id}." + Style.RESET_ALL)

def view_order(db):
    """Exibe detalhes de um pedido."""
    print_title("Visualizar Pedido")
    order_id = int(input("ID do pedido: "))
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        print(Fore.RED + "❌ Pedido não encontrado." + Style.RESET_ALL)
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
    print_title("Atualizar Status")
    order_id = int(input("ID do pedido: "))
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        print(Fore.RED + "❌ Pedido não encontrado." + Style.RESET_ALL)
        return

    print("\nStatus disponíveis:")
    print("1. Novo")
    print("2. Preparando")
    print("3. Concluído")
    status = input("Escolha o novo status (1/2/3): ")
    status_map = {"1": "Novo", "2": "Preparando", "3": "Concluído"}
    order.status = status_map.get(status, order.status)
    db.commit()
    print(Fore.GREEN + f"\n✅ Status do pedido {order_id} atualizado para '{order.status}'." + Style.RESET_ALL)

def main():
    """Menu principal."""
    db = SessionLocal()
    while True:
        clear_console()
        print_title("🍴 FoodFlow 🍴")
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
            print(Fore.BLUE + "\nObrigado por usar o FoodFlow! Até a próxima. 🍽️" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\n❌ Opção inválida. Tente novamente." + Style.RESET_ALL)

        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()
