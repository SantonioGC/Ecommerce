from auth import AuthManager

auth = AuthManager()

# Test registro
user_id = auth.register_user("test@example.com", "password123", "Juan", "Pérez")
print(f"Usuario registrado con ID: {user_id}")

# Test autenticación
user = auth.authenticate_user("test@example.com", "password123")
if user:
    print(f"Autenticación exitosa: {user['nombre']} (ID: {user['id']})")
else:
    print("Error en autenticación")