from auth import AuthManager
from products import ProductManager
from cart import CartManager
from orders import OrderManager

class EcommerceApp:
    def __init__(self):
        self.auth = AuthManager()
        self.products = ProductManager()
        self.cart = CartManager()
        self.orders = OrderManager()
        self.current_user = None
    
    def show_menu(self):
        print("\n--- Sistema Ecommerce ---")
        if not self.current_user:
            print("1. Registrarse")
            print("2. Iniciar sesion")
        else:
            print(f"Bienvenido, {self.current_user['nombre']}")
            print("3. Ver productos")
            print("4. Ver carrito")
            print("5. Ver pedidos")
            print("6. Cerrar sesion")
        print("0. Salir")
    
    def run(self):
        while True:
            self.show_menu()
            choice = input("Selecciona una opcion: ")
            
            if choice == "1":
                self.register()
            elif choice == "2":
                self.login()
            elif choice == "3" and self.current_user:
                self.show_products()
            elif choice == "4" and self.current_user:
                self.show_cart()
            elif choice == "5" and self.current_user:
                self.show_orders()
            elif choice == "6" and self.current_user:
                self.current_user = None
                print("Sesion cerrada")
            elif choice == "0":
                break
    
    def register(self):
        email = input("Email: ")
        password = input("Password: ")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        
        try:
            user_id = self.auth.register_user(email, password, nombre, apellido)
            print(f"Usuario registrado con ID: {user_id}")
        except Exception as e:
            print(f"Error en registro: {e}")
    
    def login(self):
        email = input("Email: ")
        password = input("Password: ")
        
        user = self.auth.authenticate_user(email, password)
        if user:
            self.current_user = user
            print(f"Bienvenido {user['nombre']}")
        else:
            print("Credenciales incorrectas")
    
    def show_products(self):
        products = self.products.get_all_products()
        for product in products:
            print(f"{product['id']}. {product['nombre']} - ${product['precio']} (Stock: {product['stock']})")
        
        product_id = input("ID del producto para agregar al carrito (0 para cancelar): ")
        if product_id and product_id != "0":
            self.cart.add_to_cart(self.current_user['id'], int(product_id))
            print("Producto agregado al carrito")
    
    def show_cart(self):
        cart_items = self.cart.get_cart(self.current_user['id'])
        total = 0
        for item in cart_items:
            subtotal = item['cantidad'] * item['precio']
            total += subtotal
            print(f"{item['nombre']} x{item['cantidad']} - ${subtotal}")
        print(f"Total: ${total}")

    def show_orders(self):
        orders = self.orders.get_user_orders(self.current_user['id'])
        if not orders:
            print("No hay pedidos")
            return
            
        for order in orders:
            print(f"Pedido #{order['id']} - Total: ${order['total']} - Estado: {order['estado']} - Fecha: {order['fecha_pedido']}")
        
        order_id = input("Ver detalles del pedido (ID) o 0 para volver: ")
        if order_id and order_id != "0":
            details = self.orders.get_order_details(int(order_id))
            print("Detalles del pedido:")
            for detail in details:
                subtotal = detail['cantidad'] * detail['precio_unitario']
                print(f"  {detail['nombre']} x{detail['cantidad']} - ${detail['precio_unitario']} c/u = ${subtotal}")

if __name__ == "__main__":
    app = EcommerceApp()
    app.run()