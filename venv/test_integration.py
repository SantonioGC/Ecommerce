from auth import AuthManager
from products import ProductManager
from orders import OrderManager

# Test integración completa
auth = AuthManager()
products = ProductManager()
orders = OrderManager()

# Autenticar usuario
user = auth.authenticate_user("test@example.com", "password123")
print(f"Usuario autenticado: {user['nombre']}")

# Obtener productos disponibles
available_products = products.get_all_products()
print(f"Productos disponibles: {len(available_products)}")

# Ver pedidos del usuario
user_orders = orders.get_user_orders(user['id'])
print(f"Pedidos del usuario: {len(user_orders)}")