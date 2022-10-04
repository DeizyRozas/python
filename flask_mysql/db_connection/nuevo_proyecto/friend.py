# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Amigo:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.ocupacion = data['ocupacion']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM amigos;"
    # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('mi_primer_flask_mysql').query_db(query)
    # crear una lista vacía para agregar nuestras instancias de friends
        amigos = []
    # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for amigo in results:
            amigos.append( cls(amigo) )
        return amigos

    @classmethod
    def insertar_amigo(cls,data):
        query ="INSERT INTO amigos (nombre, apellido, ocupacion) VALUES (%(vnombre)s, %(vapellido)s, %(vocc)s);"
        return connectToMySQL('mi_primer_flask_mysql').query_db( query, data )

            
