from products import ProductManager

product_manager = ProductManager()

# Test obtener todos los productos
products = product_manager.get_all_products()
print(f"Productos encontrados: {len(products)}")

# Test obtener producto por ID
if products:
    product = product_manager.get_product_by_id(products[0]['id'])
    print(f"Producto por ID: {product['nombre']}")