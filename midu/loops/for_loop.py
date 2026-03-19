# FOR
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print(fruta)

# ENUMERATE
# returns index and value
frutas = ["manzana", "pera", "mandarina"]
for idx,value in enumerate(frutas):
    print("El indice es %d y la fruta es %s" % (idx,value))

# LIST COMPREHENSION
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animles_mayus = [animal.upper() for animal in animales]
print(animles_mayus)

pares = [num for num in range(1,7) if num % 2 == 0]
print(pares)