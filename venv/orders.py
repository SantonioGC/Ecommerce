from database import Database

class OrderManager:
    def __init__(self):
        self.db = Database()
    
    def create_order(self, user_id, address_id, cart_items):
        total = sum(item['precio'] * item['cantidad'] for item in cart_items)
        
        cursor = self.db.execute_query(
            "INSERT INTO pedidos (usuario_id, direccion_id, total) VALUES (%s, %s, %s) RETURNING id",
            (user_id, address_id, total)
        )
        order_id = cursor.fetchone()['id']
        
        for item in cart_items:
            self.db.execute_query(
                "INSERT INTO pedido_items (pedido_id, producto_id, cantidad, precio_unitario) VALUES (%s, %s, %s, %s)",
                (order_id, item['producto_id'], item['cantidad'], item['precio'])
            )
        
        self.db.commit()
        return order_id
    
    def get_user_orders(self, user_id):
        cursor = self.db.execute_query(
            "SELECT * FROM pedidos WHERE usuario_id = %s ORDER BY fecha_pedido DESC",
            (user_id,)
        )
        return cursor.fetchall()