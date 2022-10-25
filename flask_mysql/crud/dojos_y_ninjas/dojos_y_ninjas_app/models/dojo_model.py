from dojos_y_ninjas_app.config.mysqlconnection import connectToMySQL
from flask import flash
from dojos_y_ninjas_app import app

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data["created_at"]
        self.updated_at= data["updated_at"]

    @classmethod
    def crear_dojo(cls, data):
        query ="INSERT INTO dojo (nombre) VALUES (%(nombre)s);"
        result= connectToMySQL("tarea_dojo_y_ninjas").query_db(query, data)
        return result

    @classmethod
    def mostrar_dojos(cls):
        query = "SELECT * FROM dojo;"
        result= connectToMySQL("tarea_dojo_y_ninjas").query_db(query)
        dojos=[]
        for dojo in result:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def un_dojo(cls,data):
        query = "SELECT * FROM dojo WHERE id = %(id)s;"
        result= connectToMySQL("tarea_dojo_y_ninjas").query_db(query, data)
        return cls(result[0])