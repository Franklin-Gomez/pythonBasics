# 03 - casting de types 
# cambiar el tipo de dato de un valor a otro tipo de dato

print(type("10")) # str

print(type( int("10") )) # int

# el signo + se utiliza para encadenar dos cadenas de textos si el primer valor es un string, si el primer valor es un numero se suman los valores

# print( "10" + 2 ) # error, no se puede sumar un string con un int
print( int("10") + 2 ) # 12, se convierte el string a int y se suman los valores
print( str(10) + "2" ) # 102, se convierte el int a string y se concatenan los valores

print( bool(0) ) # False, 0 es considerado como False
print( bool(1) ) # True, 1 es considerado como True 
print( bool(-1  )) # True, cualquier numero diferente de cero es considerado como True 

print( bool("") ) # False, una cadena vacia es considerada como False
print( bool(" ") ) # True, una cadena con un espacio es considerada como True