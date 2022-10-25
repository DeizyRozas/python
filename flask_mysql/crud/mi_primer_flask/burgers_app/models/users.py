from burgers_app.config.mysqlconnection import connectToMySQL
from burgers_app.models.burger_model import Burger
from flask import flash
import re	# el módulo regex
# crea un objeto de expresión regular que usaremos más adelante
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.password= data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # Creamos una lista para que luego podamos agregar todas las hamburguesas que están asociadas a un restaurante
        self.burgers = []


    @classmethod
    def registro( cls , data ):
        query ="INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) VALUES (%(first_name)s,%(last_name)s, %(email)s, %(password)s, NOW(),NOW());"
        return connectToMySQL('login_reg').query_db( query, data)



    @staticmethod
    def validate_user(user):
        is_valid=True
        if len(user["first_name"])<3:
            flash("Nombre debe tener al menos 3 caracteres")
            is_valid=False
        
        if len(user["last_name"])<3:
            flash(" Las name debe tener al menos 3 caracteres")
            is_valid=False

        if len(user["email"]) <3:
            flash("email debe tener +3 caracteres.")
            is_valid = False

        if len(user["password"]) < 3:
            flash("Password must be at least 3 characters.")
            is_valid = False

        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
