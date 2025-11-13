import hashlib
import secrets
from database import Database

class AuthManager:
    def __init__(self):
        self.db = Database()
    
    def hash_password(self, password):
        salt = secrets.token_hex(16)
        hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
        return hash_obj.hex(), salt
    
    def verify_password(self, password, stored_hash, salt):
        hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
        return hash_obj.hex() == stored_hash
    
    def register_user(self, email, password, nombre, apellido, telefono=None, fecha_nacimiento=None):
        password_hash, salt = self.hash_password(password)
        cursor = self.db.execute_query(
            "INSERT INTO usuarios (email, password_hash, salt, nombre, apellido, telefono, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id",
            (email, password_hash, salt, nombre, apellido, telefono, fecha_nacimiento)
        )
        user_id = cursor.fetchone()['id']
        self.db.commit()
        return user_id
    
    def authenticate_user(self, email, password):
        cursor = self.db.execute_query(
            "SELECT id, password_hash, salt, nombre, tipo_usuario FROM usuarios WHERE email = %s AND activo = TRUE",
            (email,)
        )
        user = cursor.fetchone()
        if user and self.verify_password(password, user['password_hash'], user['salt']):
            return user
        return None