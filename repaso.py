# probando 
print("Hello, World!")
#La cantidad de espacios depende de usted como programador, el uso más común es cuatro, pero tiene que ser al menos uno.
if 5 > 2:
    print("Five is greater than two!")

#Tienes que usar la misma cantidad de espacios en el mismo bloque de código, de lo contrario, Python te dará un error
"""
if 5 > 2:
    print("Cinco es mayor que dos!")
        print("Cinco es mayor que dos!")
"""
#Variables: En Python, las variables se crean cuando le asignas un valor
x = 32
y = "Mi edad"
print(x)
print(y)
#Fundición: Si desea especificar el tipo de datos de una variable, puede hacerlo con la conversión
x = str(3)    # x will be '3' es un string
y = int(3)    # y will be 3 es un entero
z = float(3)  # z will be 3.0 es un numero decimal
#obtener el tipo: Puede obtener el tipo de datos de una variable con la type()función.
x = 5
y = "John"
print(type(x))
print(type(y))
#Nombres de variables de varias palabras
myVariableName = "John" #Carmel
MyVariableName = "John" #Pascual
my_variable_name = "John" #Serpiente
#Desempaquetar una colección: Si tiene una colección de valores en una lista, tupla, etc. Python le permite extraer los valores en variables. Esto se llama desempacar .
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#apple
#banana
#cherry

#tipos de datos integrados https://www.w3schools.com/python/python_datatypes.asp
