
# 01 - sentencias condicionales ( if , elif , else )
# Permiten ejecutar bloques de cogido solo si se cumple una condición determinada.

import os

os.system("cls") # limpiar pantalla


print("\nSentencias condicionales")

#edad = 18

#if edad >= 18:
#   print("Eres mayor de edad")


print("\nSentencias condicionales con else")


# edad = 15 

# if edad >= 18: # no cumple esta condicion
#     print("Eres mayor de edad")
# else: # cumple esta condicion
#     print("Eres menor de edad")


print("\nSentencias condicionales con elif")

# Solo entrara en la primera condicion que se cumpla, si no se cumple ninguna entrara en el else
# si entra en la primera condicion no entrara en las demas, aunque se cumplan. 

# nota = 7

# if nota >= 9:
#     print("Excelente")

# elif nota >= 7:
#     print("Muy bien")

# else: # el else no es completamente necesario, pero es recomendable 
#     print("Sigue practicando")


print("\nCondiciones multiples con operadores logicos")

edad = 18
tiene_carnet = True

if edad >= 18 and tiene_carnet: # si cumple las dos condiciones 
    print("Puedes conducir")
else :
    print("No puedes conducir")

# or , si una condicion se cumple, entra en el bloque de codigo.

es_fin_de_semana = False

if not es_fin_de_semana: # si no es fin de semana , negando la condicion con not algo que ya es false, se vuelve true
    print("Puedes conducir")


print ("\nAnidar condicionales")

edad = 18
tiene_dinero = True

# no es recomendable anidar condicionales, es mejor usar operadores logicos para unir condiciones.
if edad >= 18:
    if tiene_dinero:
        print(" Puedes ir a la discoteca")
    else:
        print(" Quedate en casa")
else:
    print(" Eres menor de edad, no puedes ir a la discoteca")

# mas simplificado y mas facil de leer 
# if edad < 18: 
#     print("No puedes entrar a la discoteca")
# elif tiene_dinero:
#     print("Puedes entrar a la discoteca")
# else:
#     print("Quedate en casa")

print ("\nLa Condicion ternaria")
# una forma concisa de un if-else en una linea de codigo 

# [ codigo si se cumple la condicion ] if [ condicion ] else [ codigo si no cumple ]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje) # es menor de edad 
