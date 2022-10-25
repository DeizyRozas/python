from recetas_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from recetas_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)  

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile (r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')

class Usuario:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password =data["password"]
        self.created_at = data["created_at"]
        self.updates_at= data["updated_at"]

    @classmethod
    def crear_usuario(cls, data):
        query ="INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s,  %(email)s,  %(password)s);"
        return connectToMySQL("recetas_usuarios").query_db(query, data)

    @classmethod
    def iniciar_sesion(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("recetas_usuarios").query_db(query,data)
            # no se encontró un usuario coincidente
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def seleccionar_usuario(cls, data):
        query = "SELECT * FROM users WHERE id = %(usuario_id)s;"
        result = connectToMySQL("recetas_usuarios").query_db(query,data)
            # no se encontró un usuario coincidente
        if len(result)<1 :
            return False
        return cls(result[0])

    @staticmethod
    def validacion(usuario):
        is_valid=True
        if len(usuario["first_name"])<2:
            flash("Nombre debe tener al menos 3 caracteres", 'registro')
            is_valid=False
        
        if len(usuario["last_name"])<3:
            flash(" El apellido debe tener al menos 3 caracteres", 'registro')
            is_valid=False

        if not EMAIL_REGEX.match(usuario['email']): 
            flash("Direccion de correo electronico invalida", 'registro')
            is_valid = False
            

        if not PASSWORD_REGEX.match(usuario["password"]):
            flash("La contraseña debe tener almenos 8 caracteres, mayusculas, minusculas y numeros", 'registro')
            is_valid = False

        if usuario["password"]!= usuario["password_confirm"] :
            flash("Las contraseñas no coinciden", 'registro')
            is_valid = False
            
        return is_valid