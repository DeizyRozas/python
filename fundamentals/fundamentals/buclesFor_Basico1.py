#1.- Básico: imprime todos los números enteros del 0 al 150.
for a in range (151):
    print(a)

# 2.-Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000. 
for multiplosDe5 in range(5,1001,5):
    print(multiplosDe5)

# 3.-Contar, a la manera del Dojo: imprime números enteros del 1 al 100. 
# Si es divisible por 5, imprime "Coding” en su lugar. 
# Si es divisible por 10, imprime "Coding Dojo". 
# for numerosEnteros1_100 in range(1,100):
    if numerosEnteros1_100%5==0:
        print("Coding")
    
    if numerosEnteros1_100%10==0:
        print("coding Dojo")

    else: print(numerosEnteros1_100)



# Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, 
# e imprime la suma final.
sum=0
for sumaEnterosImpares in range(0,500001):
    if sumaEnterosImpares%3==0:
        sum+=sumaEnterosImpares
print(sum)
#41666583333
    


# Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, 
# en cuenta regresiva de 4 en 4.
for cuentaRegresivaDeA4 in range (2018,0,-4):
    print(cuentaRegresivaDeA4)



# Contador flexible: establece tres variables: lowNum, highNum, mult. 
# Comenzando en lowNum y pasando por highNum,
#  imprime solo los enteros que sean múltiplos de mult. 
# Por ejemplo, si lowNum=2, highNum=9 y mult=3. 
#  El bucle debe imprimir 3, 6, 9 (en líneas sucesivas). 

lowNum=2
highNum=9
mult=3

for contadorFlexible in range(lowNum, highNum+1):
    if contadorFlexible%mult==0:
        print(contadorFlexible)
