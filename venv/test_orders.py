from orders import OrderManager

order_manager = OrderManager()

# Test obtener pedidos de usuario
orders = order_manager.get_user_orders(1)
print(f"Pedidos del usuario 1: {len(orders)}")

