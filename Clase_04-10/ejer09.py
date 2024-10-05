"""_summary_
Colecciones de Python
"""
# Lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# tuplas
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Diccionarios
diccionario = {
    "ci": 1,
    "nombre": "Juan",
    "edad": 30,
    "estado civil": "S"
}

# Set
set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

def sumar(a, b):
    return a + b,a,b

print(sumar(1,2))
print(sumar(2,2))
print(sumar(3,2))
v1,v2,v3 = sumar(4,5)
print(v1,v2,v3)