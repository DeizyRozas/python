# print(type(24))
# print(type(3.9))
# print(type(3j))

# int_to_float = float(35) 
# float_to_int = int(44.2)  
# int_to_complex = complex(35) 
# print(int_to_float)  #35.0
# print(float_to_int)  #42
# print(int_to_complex) #35+0j
# print(type(int_to_float)) #float
# print(type(float_to_int))  #int
# print(type(int_to_complex)) #complex

# import random
# print(random.randint(2,5)) # proporciona un número aleatorio entre 2 y 5

# edad= str(29)
# print("Aun tengo"+ edad)
# print(type(edad))

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"Mi nombre es {first_name} {last_name} y tengo {age} años de edad.")

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("Mi nombre es {} {} y tengo {} años de edad.".format(last_name, age, first_name))
# # salida: Mi nombres es Zen Coder y tengo 27 años de edad.
# # print("Mi nombre es {} {} y tengo {} años de edad.".format(age, first_name, last_name))
# # # salida: Mi nombre es 27 Zen y tengo Coder años de edad.

# hw = "Hola %s" % "mundo" 	# con valores literales
# py = "Me encanta Python %d" % 3 
# print(hw, py)
# # salida: Hola mundo Me encanta Python 3
# name = "Zen"
# age = 27
# print("Mi nombre es %s y tengo %d" % (name, age))		# o con variables
# # salida: Mi nombre es Zen y tengo 27

# x = "hola mundo"
# print(x.title())

# frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
# vegetales = ['lechuga', 'pepino', 'zanahorias']
# frutas_y_vegetales = frutas + vegetales
# print(frutas_y_vegetales)
# ensalada = 3 * vegetales
# print(ensalada)

# x = [99,4,2,5,-3]
# print(x[:])
# # la salida sería [99,4,2,5,-3]
# print(x[1:])
# # la salida sería [4,2,5,-3];
# print(x[:4])
# # la salida sería [99,4,2,5]
# print(x[2:4])
# # la salida sería [2,5];


# perro = ("Canis Familiaris", "perro", "carnívoro", 12)
# perro = perro + ("doméstico",)
# print(perro)
# # el resultado...
# #("Canis Familiaris", "Perro", "carnívoro", 12, "doméstico")
# perro = perro[:3] + ("el mejor amigo del hombre",) + perro[4:]
# print(perro)
# el resultado es...
#("Canis Familiaris", "Perro", "carnívoro", "el mejor amigo del hombre", "doméstico")

findesemana = {"Dom": "Domingo", "Sáb": "Sábado"} # notación literal
capitales = {} # crea un diccionario vacío y luego agrega valores
capitales["svk"] = "Bratislava"
capitales["deu"] = "Berlin"
capitales["dnk"] = "Copenhagen"

print(capitales)

print(findesemana["Dom"])
print(capitales["svk"])
value_removed = capitales.pop('svk') # eliminará la clave 'svk' y devolverá su valor
del capitales['dnk'] # eliminará la clave y no devolverá nada










