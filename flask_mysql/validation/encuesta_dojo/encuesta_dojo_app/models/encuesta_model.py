from encuesta_dojo_app.config.mysqlconnection import connectToMySQL
from flask import flash
from encuesta_dojo_app import app        


class Encuesta:
    def __init__(self,data):
        self.nombre = data['nombre']
        self.ubicacion = data['ubicacion']
        self.idioma = data["idioma"]
        self.comentario = data["comentario"]
        self.created_at = data["created_at"]
        self.updated_at= data["updated_at"]

    @classmethod
    def subir_info(cls,data):
        query="INSERT INTO dojos (nombre, ubicacion, idioma, comentario) VALUES (%(nombre)s, %(ubicacion)s,  %(idioma)s,  %(comentario)s);"
        return connectToMySQL("esquema_encuesta_dojo").query_db(query, data)

    @classmethod
    def mostrar_info(cls):
        query = "SELECT * FROM dojos; "
        results = connectToMySQL('esquema_encuesta_dojo').query_db(query)
        dojos = []

        for d in results:
            dojos.append(cls(d))
        return dojos
