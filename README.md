# **FoodFlow** 🍴  
> **Simulador de Pedidos de Restaurante**: Um sistema funcional e interativo para gerenciar cardápios, pedidos e status de forma simples e eficiente.

---

## **Sobre o Projeto**
O **FoodFlow** é uma aplicação backend desenvolvida em **Python**, utilizando **FastAPI**, **SQLAlchemy** e **SQLite**. O objetivo do projeto é simular o funcionamento de um restaurante, permitindo:
- Gerenciar o cardápio (adicionar, listar, editar e remover itens).
- Criar e gerenciar pedidos (adicionar itens, visualizar total, atualizar status).
- Navegar por um menu interativo diretamente no terminal.

Com o **FoodFlow**, você tem uma solução prática e funcional para explorar conceitos de backend e gerenciamento de banco de dados.

---

## **Funcionalidades**
- **Cardápio**:
  - Adicionar itens ao cardápio.
  - Listar itens disponíveis.
  - Editar ou remover itens (futuramente, se necessário).

- **Pedidos**:
  - Criar pedidos.
  - Adicionar itens do cardápio aos pedidos.
  - Atualizar o status dos pedidos (Novo, Preparando, Concluído).
  - Calcular o total automaticamente com base nos itens adicionados.

- **Banco de Dados**:
  - Persistência dos dados com **SQLite**.
  - Modelos bem estruturados utilizando **SQLAlchemy**.

---

## **Pré-requisitos**
Antes de começar, você precisará ter instalado em sua máquina:
- **Python 3.8+**
- Um editor de texto ou IDE (como VS Code)

---

## **Como Rodar o Projeto**

### **1. Clone o Repositório**
```bash
git clone https://github.com/O-Farias/foodflow.git
cd foodflow 
```

### **2. Crie um Ambiente Virtual**
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate 
```

### **3. Instale as Dependências**
```bash
pip install -r requirements.txt 
```

### **4. Rode o Projetos**
```bash
python app/main.py
```

## **Como Usar**

1. Quando rodar o programa, você verá o menu principal no terminal:

```plaintext
🍴 FoodFlow 🍴
1. Listar cardápio
2. Adicionar item ao cardápio
3. Criar pedido
4. Adicionar item ao pedido
5. Visualizar pedido
6. Atualizar status do pedido
7. Sair
Escolha uma opção:
```

2. Siga as instruções para interagir com o sistema:
   - Adicione itens ao cardápio.
   - Crie pedidos e adicione itens ao pedido.
   - Atualize o status ou visualize os detalhes de um pedido.

## **Tecnologias Utilizadas**

- **Python 3.10**
- **FastAPI** - Framework web para a API.
- **SQLAlchemy** - ORM para gerenciar o banco de dados.
- **SQLite** - Banco de dados relacional leve e integrado.
- **Colorama** - Estilização das mensagens no terminal.

## **Licença**

Esse projeto está sob a licença **MIT**.
