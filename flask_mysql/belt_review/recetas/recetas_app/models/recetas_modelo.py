import re
from unittest import result
from recetas_app import app
from recetas_app.config.mysqlconnection import connectToMySQL
from flask import flash
from recetas_app.models.usuarios_modelo import Usuario

# FECHA_REGEX = re.compile(r'^([0-2][0-9]|(3)[0-1])(-)(((0)[0-9])|((1)[0-2]))(-)\d{4}$')

class Receta:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.under = data["under"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.date_made = data["date_made"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id =data["user_id"]
        self.usuarios=[]

    @classmethod
    def obtener_recetas(cls):
        query = "SELECT * FROM recipes;"
        results= connectToMySQL("recetas_usuarios").query_db(query)
        recetas=[]

        for r in results:
            recetas.append(cls(r))
        return recetas

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id= %(id)s"
        result= connectToMySQL("recetas_usuarios").query_db(query, data)
        return cls(result[0])

    @classmethod
    def obtener_recetas_con_usuarios(cls):
        query = "SELECT * FROM recipes JOIN users on recipes.user_id=users.id;"
        results= connectToMySQL("recetas_usuarios").query_db(query)
        todas_recetas_con_usuarios=[]

        for receta in results:
            objeto_receta= cls(receta)
            objeto_receta.usuarios.append(Usuario(receta))
            todas_recetas_con_usuarios.append(objeto_receta)
        return todas_recetas_con_usuarios

    @classmethod
    def receta_de_un_usuario(cls, data):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s"
        resultado = connectToMySQL("recetas_usuarios").query_db(query, data)
        una_receta=cls(resultado[0])
        una_receta.usuarios.append(Usuario(resultado[0]))
        return una_receta

    

    

    @classmethod
    def crear_receta(cls, data):
        query ="""INSERT INTO recipes (name, under, description, instruction, date_made, created_at, updated_at, user_id) 
                            VALUES (%(name)s, %(under)s,  %(description)s,  %(instruction)s, %(date_made)s, NOW(), NOW(), %(user_id)s);"""
        resultado= connectToMySQL("recetas_usuarios").query_db(query, data)
        return resultado

    @classmethod
    def editar_receta(cls,data):
        query = "UPDATE recipes SET  name=%(name)s, under=%(under)s, description=%(description)s, instruction=%(instruction)s, date_made=%(date_made)s, updated_at=NOW() WHERE id=%(id)s;"
        resultado=connectToMySQL("recetas_usuarios").query_db(query,data)
        return resultado
        
    @classmethod
    def eliminar_receta(cls, data):
        query = "DELETE FROM recipes WHERE id=%(id)s; "
        resultado= connectToMySQL("recetas_usuarios").query_db(query,data)
        return resultado

    @staticmethod
    def validacion(receta):
        is_valid=True
        if len(receta["date_made"])<8:
            flash("Rellenar campo obligatorio", 'editar')
            is_valid=False

        is_valid=True
        if len(receta["name"])<3:
            flash("Rellenar campo obligatorio: Nombre", "editar")
            is_valid = False
        
        is_valid=True
        if len(receta["description"])<3:
            flash("Rellenar campo obligatorio: Descripción", "editar")
            is_valid = False

        is_valid=True
        if len(receta["instruction"])<3:
            flash("Rellenar campo obligatorio: instrucciones", "editar")
            is_valid = False

        is_valid=True
        if len(receta["name"])<3:
            flash("Rellenar campo obligatorio: Nombre", "crear_receta")
            is_valid = False
        
        is_valid=True
        if len(receta["description"])<3:
            flash("Rellenar campo obligatorio: Descripción", "crear_receta")
            is_valid = False

        is_valid=True
        if len(receta["instruction"])<3:
            flash("Rellenar campo obligatorio: instrucciones", "crear_receta")
            is_valid = False

        if len(receta["date_made"])<8:
            flash("Rellenar campo obligatorio", 'crear_receta')
            is_valid=False

        
        return is_valid