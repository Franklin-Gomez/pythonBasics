
# 05 - entrada de usuario (( input ()  ) - version sdimplificada )
# input() es una funcion que permite al usuario ingresar datos por teclado

## print("Hola, por favor ingresa tu nombre: ")
## nombre = input() 
## print("Hola " + nombre + ", bienvenido a Python!")

nombre = input("Hola, por favor ingresa tu nombre: ") # otra forma de usar input() con un mensaje
print("Hola " + nombre + ", bienvenido a Python!")

age = input("Por favor ingresa tu edad: ") # input() siempre devuelve un string
#print("Tu edad es: " + age + 20 + " años") # concatenando un string con

## esto no funciona o nos muestra un error , ya que lo que sea que nos mande input() es un strin no importa si lo que escribe el usuario es un numero

age = int( age ) # convertimos el string a un entero
print(f"Tu edad es: {age + 20} años")  

# pedir varios datos al usuario y mostrarlos en pantalla
print("Obtener varios datos de una vez")

country , city  = input ( " En que pais y ciudad vives? \n " ).split() # split() divide el string en una lista de palabras separadas por espacios

print(f"Vives en {city} , {country}")
