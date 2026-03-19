print("Bucle while\n")

# Simple condition
counter = 0
while counter <= 6:
    print(counter)
    counter += 1

# Break
print("\nBreak\n")
counter2 = 0

while True:
    print(counter2)
    counter2 += 1
    if counter2 == 6:
        break

"""
num = -1
while num < 0:
    num = int(input("[+] Introduce un número:"))
    if num < 0:
        print("El numero debe ser positivo")
else:
    print(f"El numero que has introducido es el {num}")
"""

# try except
num = -1
while num < 0:
    try:
        num = int(input("[+] Introduce un número:"))
        if num < 0:
            print("El numero debe ser positivo")
    except:
        print("Lo que introduces debe ser un numero, intenta de nuevo")
else:
    print(f"El numero que has introducido es el {num}")
