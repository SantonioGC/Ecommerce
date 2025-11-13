from flask import Flask, request, jsonify
from auth import AuthManager
from products import ProductManager
from cart import CartManager
from orders import OrderManager

app = Flask(__name__)
auth = AuthManager()
products = ProductManager()
cart = CartManager()
orders = OrderManager()

@app.route('/')
def index():
    return jsonify({
        'message': 'API Ecommerce funcionando',
        'endpoints': {
            '/api/register': 'POST - Registrar usuario',
            '/api/login': 'POST - Iniciar sesión',
            '/api/products': 'GET - Listar productos',
            '/api/cart': 'GET - Ver carrito',
            '/api/cart/add': 'POST - Agregar al carrito',
            '/api/orders': 'GET - Listar pedidos',
            '/api/orders/create': 'POST - Crear pedido'
        }
    })

if __name__ == '__main__':
    app.run(debug=True)