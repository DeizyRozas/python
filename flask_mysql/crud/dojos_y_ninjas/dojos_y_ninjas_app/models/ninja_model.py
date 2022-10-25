from dojos_y_ninjas_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
from dojos_y_ninjas_app import app        


class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data["apellido"]
        self.dojo_id = data["dojo_id"]
        self.edad = data["edad"]
        self.created_at = data["created_at"]
        self.updated_at= data["updated_at"]

    @classmethod
    def crear_ninja(cls, data):
        query ="INSERT INTO ninjas (dojo_id, nombre, apellido, edad) VALUES (%(dojo_id)s, %(nombre)s, %(apellido)s,  %(edad)s);"
        result= connectToMySQL("tarea_dojo_y_ninjas").query_db(query, data)
        return result

    @classmethod
    def ninjas_por_dojo(cls,data):
        query="SELECT * from ninjas WHERE dojo_id=%(id)s"
        result= connectToMySQL("tarea_dojo_y_ninjas").query_db(query, data)
        ninjas=[]
        for ninja in result:
            ninjas.append(cls(ninja))
        return ninjas