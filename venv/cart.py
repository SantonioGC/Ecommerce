from database import Database

class CartManager:
    def __init__(self):
        self.db = Database()
    
    def add_to_cart(self, user_id, product_id, quantity=1):
        cursor = self.db.execute_query(
            "INSERT INTO carrito (usuario_id, producto_id, cantidad) VALUES (%s, %s, %s) ON CONFLICT (usuario_id, producto_id) DO UPDATE SET cantidad = carrito.cantidad + EXCLUDED.cantidad RETURNING id",
            (user_id, product_id, quantity)
        )
        self.db.commit()
        return cursor.fetchone()['id']
    
    def get_cart(self, user_id):
        cursor = self.db.execute_query(
            "SELECT c.*, p.nombre, p.precio FROM carrito c JOIN productos p ON c.producto_id = p.id WHERE c.usuario_id = %s",
            (user_id,)
        )
        return cursor.fetchall()
    
    def remove_from_cart(self, user_id, product_id):
        cursor = self.db.execute_query(
            "DELETE FROM carrito WHERE usuario_id = %s AND producto_id = %s RETURNING id",
            (user_id, product_id)
        )
        self.db.commit()
        return cursor.fetchone() is not None
    
    def clear_cart(self, user_id):
        cursor = self.db.execute_query(
            "DELETE FROM carrito WHERE usuario_id = %s RETURNING id",
            (user_id,)
        )
        self.db.commit()
        return cursor.rowcount