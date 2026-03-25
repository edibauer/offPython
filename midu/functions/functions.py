### Funciones ###

""" Definicion
def function_name(param1, param2, param3,...):
    # docstring
    # body
    # return (optional)
"""

# Ejemplos
def saludar():
    print("I dont take mistakes")

# Example with params
def saludar_a(name: str) -> str:
    print("i dont make mistakes %s" % name)

# Functions with more params
def sumar(num1: int, num2: int) -> int:
    return num1 + num2

# Fixing function
"""
def sumar(num1: int, num2: int) -> int | None: # Agregamos None al tipo de retorno
    try:
        return num1 + num2
    except TypeError:
        print("Error: Los valores deben ser números")
        return None
"""
# Best practices
"""

def sumar(num1: int, num2: int) -> int:
    return num1 + num2  # Si falla, el programa lanza la excepción y listo.
"""

# docstring
def restar(num1: int, num2: int) -> int:
    """
    Resta dos números
    Args:
        num1: El primer número
        num2: El segundo número
    Returns:
        La resta de los dos números
    """
    return num1 - num2

# Default params
def multiplicar(num1: int, num2: int = 2) -> int:
    return num1 * num2

# position params
def describir_persona(name, age, sex):
    print(f"Nombre: {name}, Edad: {age}, Sexo: {sex}")

# args wuth length variable
def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

# Args key-value with length variable
def mostrar_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# calling
if __name__ == "__main__":
    saludar()
    saludar_a("edibauer")
    print(sumar(3,6))
    print(restar(10,4))
    # print(restar.__doc__)
    # help(restar)
    print(multiplicar(3,4))
    print(multiplicar(3))

    # position args
    describir_persona("edibauer", 31, "masculino")

    # keyword args
    describir_persona(age=31, sex="masculino", name="edibauer")

    # args with length variable
    print(sumar_numeros(1,2,3,4,5,6))

    # args key-value with length variable
    mostrar_info(name="edibauer", age=31, sex="masculino")



