# Suma de numero pares
# Calcula la suma de los numeros pares entre 1 y 20 (inclusivo) usando un bucle while

counter = 1
sum = 0
while counter <= 20:
    # print(counter)
    if counter % 2 == 0:
        sum += counter
    counter += 1

print("La suma de los numero es %d" % sum)