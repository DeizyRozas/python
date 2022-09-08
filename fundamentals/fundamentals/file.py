num1 = 42                       #declaracion de variables   tipo de dato primitivo: numero entero
num2 = 2.3                            # numero punto flotante
boolean = True                         # booleano
string = 'Hello World'                  # cadena
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']           #inicializa lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}    # inicializa diccionario
fruit = ('blueberry', 'strawberry', 'banana')   # inicializa una tupla
print (type(fruit))                             #type check
print(pizza_toppings[1])                        #accede a un valor de la lista
pizza_toppings.append('Mushrooms')              #agrega un valor a la lista
print(person['name'])                            #"accede a un valor del diccionario"
person['name'] = 'George'                        # cambia un valor del diccionario
person['eye_color'] = 'blue'                     #agrega un valor al diccionario
print(fruit[2])                                 #accede a un valor de la tupla

if num1 > 45:                                   # Condicional IF
    print("It's greater")                       #log statement
else:                                            #condicional ELSE
    print("It's lower")

if len(string) < 5:                             #length check
    print("It's a short word!")
elif len(string) > 15:                           #condicional ELSE IF
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):                              # FOR LOOP start 0, stop <5, ++.
    print(x)
for x in range(2,5):                            # FOR LOOP start 2, stop <4, ++.
    print(x)
for x in range(2,10,3):                         # FOR LOOP start 2, stop <10, incrementa en 3.
    print(x)
x = 0
while(x < 5):                                   #while loop start 0, stop <5
    print(x)
    x += 1                                     #incrementa en 1

pizza_toppings.pop()                         # elimina el ultimo valor de la lista
pizza_toppings.pop(1)                        # elimina un valor dirigido de la lista

print(person)
person.pop('eye_color')                      #elimina un valor del diccionario
print(person)

for topping in pizza_toppings:                 #FOR LOOP secuencia
    if topping == 'Pepperoni':
        continue                            # continue
    print('After 1st if statement')
    if topping == 'Olives':
        break                               # break

def print_hello_ten_times():                #funcion
    for num in range(10):                   # argumento de la funcion
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):                 
    for num in range(x):
        print('Hello')

print_hello_x_times(4)                      #parametro de la funcion x=4

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section             comment multilinea
""" 

# print(num3)                               comment 1 sola linea     NameError
# num3 = 72                                 name <num3> is not defined
# fruit[0] = 'cranberry'                   cambia valor de un indice de la tupla, TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team'])            KeyError
# print(pizza_toppings[7])                 IndexError: list index out of range 
#   print(boolean)                          identationError
# fruit.append('raspberry')                agrega un valor a la tupla, AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)                             borrar valor de la tupla, AttributeError: 'tuple' object has no attribute 'pop'