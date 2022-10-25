import crear_usuarios_app
from crear_usuarios_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from crear_usuarios_app import app
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)  

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
PASSWORD_REGEX = re.compile (r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')

class Usuario:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data["apellido"]
        self.correo_electronico = data["correo_electronico"]
        self.contraseña =data["contraseña"]
        self.created_at = data["created_at"]
        self.updated_at= data["updated_at"]

    @classmethod
    def mostrar_usuarios(cls):
        query = "SELECT * FROM usuarios; "
        results = connectToMySQL('esquema_usuarios').query_db(query)
        usuarios = []
        

        for u in results:
            usuarios.append(cls(u))
        return usuarios

    @classmethod
    def crear_usuarios(cls, data):
        query ="INSERT INTO usuarios (nombre, apellido, correo_electronico, contraseña) VALUES (%(nombre)s, %(apellido)s,  %(correo_electronico)s,  %(contraseña)s);"
        return connectToMySQL("esquema_usuarios").query_db(query, data)

    @classmethod
    def borrar(cls,data):
        query = "DELETE FROM usuarios WHERE id = %(id)s; "
        return connectToMySQL("esquema_usuarios").query_db(query, data)

    @classmethod
    def editar(cls,data):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, contraseña=%(contraseña)s, updated_at=NOW() WHERE id= %(id)s"
        return connectToMySQL("esquema_usuarios").query_db(query, data)

    @classmethod
    def mostrar_usuario(cls,data):
        query = "SELECT * FROM usuarios WHERE id= %(id)s"
        mostrar_usuario=connectToMySQL("esquema_usuarios").query_db(query, data)
        return cls(mostrar_usuario[0])

    @classmethod
    def iniciar_sesion(cls,data):
        query = "SELECT * FROM usuarios WHERE correo_electronico = %(correo_electronico)s;"
        result = connectToMySQL("esquema_usuarios").query_db(query,data)
        # no se encontró un usuario coincidente
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validacion(usuario):
        is_valid=True
        if len(usuario["nombre"])<2:
            flash("Nombre debe tener al menos 3 caracteres", 'registro')
            is_valid=False
        
        if len(usuario["apellido"])<3:
            flash(" El apellido debe tener al menos 3 caracteres", 'registro')
            is_valid=False

        if not EMAIL_REGEX.match(usuario['correo_electronico']): 
            flash("Direccion de correo electronico invalida", 'registro')
            is_valid = False
            

        if not PASSWORD_REGEX.match(usuario["contraseña"]):
            flash("La contraseña debe tener almenos 8 caracteres, mayusculas, minusculas y numeros", 'registro')
            is_valid = False

        if usuario["contraseña"]!= usuario["confirmacion_contraseña"] :
            flash("Las contraseñas no coinciden", 'registro')
            is_valid = False
        
        return is_valid

