from database import Database

try:
    db = Database()
    print("Conectado a PostgreSQL correctamente")
    
    # Test simple query
    cursor = db.execute_query("SELECT version()")
    version = cursor.fetchone()
    print(f"Version de PostgreSQL: {version['version']}")
    
    db.close()
except Exception as e:
    print(f"Error de conexion en la DB: {e}")