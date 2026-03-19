# Factorial de un numero
# Pide al usuario que ingrese un numero y calcula el factorial de ese numero

if __name__ == "__main__":
    
    flag = True
    fac = 1
    while flag:
        try:
            x = int(input("[+] Ingresa un numero positivo: "))
            if x > 0:
                for i in range(1, x +1):
                    fac *= i
            flag = False
        except:
            print("Debes ingresar un numero")
    
    print("El factorial del numero es: %d" % fac)