from crear_usuarios_app.config.mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self,data):
        self.id = data["id"],
        self.nombre = data['nombre'],
        self.apellido = data["apellido"],
        self.correo = data["correo_electronico"],
        self.created_at = data["creado_en"],
        self.actualizado_en= data["actualizado_en"]

    @classmethod
    def mostrar_usuarios(cls):
        query = "SELECT * FROM usuarios; "
        results = connectToMySQL('esquema_usuarios').query_db(query)
        usuarios = []

        for usuario in results:
            usuarios.append(cls(usuario))
        
        return usuarios

    @classmethod
    def crear_usuarios(cls, data):
        query ="INSERT INTO usuarios (nombre, especie) VALUES (%(nombre)s, %(apellido)s, %(correo_electronico)s);"
        return connectToMySQL("esquema_usuarios").query_db(query, data)