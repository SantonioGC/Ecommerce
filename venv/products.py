from database import Database

class ProductManager:
    def __init__(self):
        self.db = Database()
    
    def get_all_products(self, active_only=True):
        query = "SELECT * FROM productos"
        if active_only:
            query += " WHERE activo = TRUE"
        cursor = self.db.execute_query(query)
        return cursor.fetchall()
    
    def get_product_by_id(self, product_id):
        cursor = self.db.execute_query(
            "SELECT * FROM productos WHERE id = %s AND activo = TRUE",
            (product_id,)
        )
        return cursor.fetchone()
    
    def get_products_by_category(self, category_id):
        cursor = self.db.execute_query(
            "SELECT * FROM productos WHERE categoria_id = %s AND activo = TRUE",
            (category_id,)
        )
        return cursor.fetchall()
    
    def update_stock(self, product_id, quantity):
        cursor = self.db.execute_query(
            "UPDATE productos SET stock = stock - %s WHERE id = %s AND stock >= %s RETURNING id",
            (quantity, product_id, quantity)
        )
        success = cursor.fetchone() is not None
        if success:
            self.db.commit()
        return success