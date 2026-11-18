###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###


print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
print("franklin \nCartagena")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
entero = int(cadena)
flotante = float(entero)
entero_de_flotante = int(3.99)
print(" el flotante 3.99 al convertirlo a entero se redondea hacia abajo, por lo que el resultado es 3")

print(f"Cadena: {type(cadena)}, Entero: {type(entero)}, Float: {type(flotante)}, Entero de float: {type(entero_de_flotante)}")


print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
nombre, edad , altura = input("Ingrese su nombre , edad y altura  separelos por espacio :  \n" ).split()
print( f"su nombre = {nombre} , su edad = {edad} , su altura = {altura}" )

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

### Completa aquí
import math

pi = math.pi
redonde = round(pi)
division = redonde // 2
print(division)