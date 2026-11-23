 

# 03 - listas 
# Secuencias mutables de elementos
# Pueden contener elementos de diferentes tipos 


# Creacion de listas 
print("\nCrear listas")

lista1 = [1,2,3,4] # lista de enteros
lista2 = [ "manzana" , "peras" , "platanos"] # lista de cadenas 
# lista3 = [ 1 , "hola" , True ] # lista de tipos mixtos , esta esta bien pero activamos el stric y se aloca el cachon 

lista_vacia = []
lista_de_listas = [ [1,2] , [3,4] ]
matrix = [ [1,2] , [3,4] , [ 5 , 6] ]

# Acceso a elementos por indices 
print("\nAcceso a elementos por indices")
# print(lista2[0]) # manzanas
# print(lista2[1]) # peras
# print(lista2[-1]) #platanos, pero esta va de atras para adelante
# print(lista2[-2]) #peras
# print( lista_de_listas[1][0]) # 3

# Slicing ( rebanado ) de listas 

lista1 = [1,2,3,4,5]
#lista1[ desde : hasta : paso ]

# print(lista1[1:2]) # [ 2 ] , indice  inicial  hasta el indice 2 pero sin incluirlo 
# print(lista1[1:4]) # [ 2 , 3 , 4 ]
# print(lista1[:3]) # [ 1 , 2 , 3 ]
# print(lista1[3:]) # [ 4 , 5 ]
# print(lista1[:]) # crea una copia

# Hay mas magia
lista1 = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ]
# print(lista1[::2]) # para devolver indices pares 
# print(lista1[::-1]) # para devolver indices inverso

# modificar la lista
lista1[2] = 10 # reemplaza el valor de esa posicion

# añadir elementos a una lista
lista1 = [ 1 , 2 , 3]

#forma larga y menos eficiente 
lista1 = lista1 + [ 4 , 5 , 6 ] # concatenar 

#forma  corta y mas eficiente 
lista1 += [ 7, 8 , 9]

print(lista1) # [ 1, 2, 3, 4, 5, 6 , 7, 8 , 9]


