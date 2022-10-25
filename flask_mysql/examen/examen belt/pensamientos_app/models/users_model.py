from pensamientos_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from pensamientos_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)  

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile (r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password =data["password"]
        self.created_at = data["created_at"]
        self.updated_at= data["updated_at"]
        self.likes=[]

    @classmethod
    def register(cls, data):
        query ="INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s,  %(email)s,  %(password)s);"
        result= connectToMySQL("panel_de_los_pensamientos").query_db(query, data)
        return result

    @classmethod
    def login(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("panel_de_los_pensamientos").query_db(query,data)
            # no se encontró un usuario coincidente
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def select_logged_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        result = connectToMySQL("panel_de_los_pensamientos").query_db(query,data)
            # no se encontró un usuario coincidente
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_by_id(cls,data):
        query="SELECT * FROM users WHERE id=%(user_id)s"
        result = connectToMySQL("panel_de_los_pensamientos").query_db(query,data)
        return cls(result[0])

    


    @staticmethod
    def validation(user):
        is_valid=True
        if len(user["first_name"])<2:
            flash("Nombre debe tener al menos 3 caracteres", 'register')
            is_valid=False
        
        if len(user["last_name"])<3:
            flash(" El apellido debe tener al menos 3 caracteres", 'register')
            is_valid=False

        if not EMAIL_REGEX.match(user['email']): 
            flash("Direccion de correo electronico invalida", 'register')
            is_valid = False
            

        if not PASSWORD_REGEX.match(user["password"]):
            flash("La contraseña debe tener almenos 8 caracteres, mayusculas, minusculas y numeros", 'register')
            is_valid = False

        if user["password"]!= user["password_confirm"] :
            flash("Las contraseñas no coinciden", 'register')
            is_valid = False
            
        return is_valid