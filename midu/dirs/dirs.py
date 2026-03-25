# ex
persona = {
    "nombre": "edibauer",
    "edad": 31,
    "es_estudiante": True,
    "calificaciones": [10,9,10],
    "redes": {
        "x": "@edibauer",
        "github": "@edibauer",
        "linkedin": "@edibauer"
    }

}

# Accesing elements
print(persona["nombre"])
print(persona["calificaciones"][1])
print(persona["redes"]["github"])
print(persona["edad"])

# Changing values
persona["edad"] = 30
print(persona["edad"])

# delete
del persona["es_estudiante"]
print(persona)

age = persona.pop("edad")
print(f"age: {age}")
print(persona)

# overwrite a dict with another dict
a = {
    "name": "edibauer",
    "age": 25
}

b = {
    "name": "edgerunner",
    "is_edegerunner": True
}

a.update(b)
print(a)

# is in
print("\n IS IN")
print("name" in persona) # false
print("calificaciones" in persona) # true
print("Is in ex")
print("edibauer" in persona.values()) # true

# get keys
print("\n GET KEYS")
print(persona.keys())
print(type(persona.keys()))

# get values
print("\n GET VALUES")
print(persona.values())

# gete keys and values
print("\n GET KEYS AND VALUES")
print(persona.items())
