print("Creacion de listas\n")
lista1 = [1,2,3,4,5,6]
lista2 = ["manzanas", "peras", "platanos"]
lista3 = [1, "bola", 3.14, True]

empty_list = []
lista_de_listas = [[1,2],[3,4]]
matrix = [[1,2], [3,4],[5,6]]

print(lista1)
print(lista2)
print(lista3)
print(empty_list)
print(lista_de_listas)
print(matrix)

# Acceso a lemento sor indice
print("Accesos a elementos por indice\n")
print(lista2[0]) # manzanas
print(lista2[1]) # peras
print(lista2[-1]) # platanos
print(lista2[-2]) # peras

# Slicing de listas
lista1 = [1,2,3,4,5]
print(lista1[1:4]) # [2,3,4]
print(lista1[:3]) # [1,2,3]
print(lista1[3:]) # [4,5]
print(lista1[:]) # [1,2,3,4,5]

# Steps
lista1 = [1,2,3,4,5,6,7,8,9,10]
# print(lista1[desde:hasta:paso])
print(lista1[::2]) # [1,3,5,7,9]
print(lista1[::-1]) # reverse
print(lista1[1::2]) # [2,4,6,8,10]

# Modifying a list
lista1[0] = 15
print(lista1)

# Adding elements into a list
lista1 = [1,2,3]
lista1 = lista1 + [4,5,6]
print(lista1)
lista1 += [7,8,9] # much better
print(lista1)