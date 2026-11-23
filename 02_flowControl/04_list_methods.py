
# 04 - Listas Metodos 
# Pueden contener elementos de diferentes tipos 

lista1 = ['a', 'b', 'c', 'd']

# añadir o insertar elementos a la lista 
lista1.append('e') # Añade un elemento al final
lista1.insert(1, '@') # ( posicion , elemento ) , insertamos un elemento en la posicion que indiquemos
lista1.extend(["correr" , "caminar"]) # agrega elementos al final 

# Eliminar elements de la lista 
lista1.remove("@") # Eliminar la primera aparicion del "@" , OJO!! Solo elimna la primera aparicion
lista1.pop() #Elimina el ultimo elemento de la lista y ademas de lo devuelve
lista1.pop(1) # Elimina el segundo elemento de la lista, Elimina la posicion que le pasemos

del lista1[-1] # eliminar por lo bestia
# lista1.clear() # Eliminar todos los elementos de la lista 

# Eliminar un rango de elementos 
lista2 = ["panda" , "oso" , "gato" , "tigre"]
del lista2[1:3] # ['panda', 'tigre']

# Mas metodos utiles 

number = [ 3, 10, 2 , 8, 99, 101]

order = sorted( number )  # Ordenar de forma ascendente , pero No modifica la lista original, sino que crea un nueva lista 

number.sort() # Ordenar de forma ascendente , modifica la lista

frutas = [ "pera" , "manzana" , "limon" , "manzana" ]


frutas.sort(key=str.lower) # para que compare en lowercase ( minusculas )
order_frutas = sorted( frutas ) # Ordena la lista OJO!!! es sencible a las mayusculas, las mayusculas irian primero 


# Mas cositas utiles 
animales = ["panda" , "oso" , "gato" , "tigre" , "panda"]

len( animales ) # nos da el tamaño de la lista 
animales.count("panda") # Cuantas veces aparece el elemento 

find = "panda" in animales # true - false , Compruba si hay "panda" en la lista de animales 