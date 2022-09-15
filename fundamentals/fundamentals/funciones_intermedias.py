x = [ [5,2,3], [10,8,9] ]
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# #Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].

# def cambiarValor():
#     x[1][0]=15
#     return x

# x=cambiarValor()
# print(x)

## Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.

# estudiantes[0]["last_name"]='Bryant'
# print(estudiantes)

# En el directorio_deportes, cambia "Messi" por "Andrés".

# directorio_deportes['fútbol'][0]=  "Andrés"
# print(directorio_deportes)

# #Cambia el valor 20 en z a 30.

# z[0]["x"]=30
# print(z)


# Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, 
# la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(estudiantes):
#     for i in estudiantes:
#         valor=list(i.items())
#         print(valor[0][0], "-", valor[0][1], ',', valor[1][0], "-", valor[1][1])

# iterateDictionary(estudiantes)
# # debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas; un bonus para que aparezcan exactamente como se muestra a continuación)

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes)
#  debería generar: Michael
# John
# Mark
# KB


# def iterateDictionary2(alguna_clave, estudiantes) :
#     for i in estudiantes:
#         clave=list(i.keys())
#         valor=list(i.values())

        
#         if clave[0]==alguna_clave:
#             print(valor[0])

#         else: print(valor[1])
        


# iterateDictionary2("first_name", estudiantes)
# iterateDictionary2("last_name", estudiantes)


# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
# imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la 
# lista de cada clave. Por ejemplo:

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# # salida:
# 7 UBICACIONES
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORES
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


def printInfo(some_dict):
    for i in some_dict:
        valores= list(some_dict[i])
        print (len(some_dict[i]), i.upper())
        
        for iterador in valores:
            print(iterador)


printInfo(dojo)