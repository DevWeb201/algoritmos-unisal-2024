"""
Introduzca los datos de un rectángulo y calcula su perimetro y area
perimetro = lado mas ancho por 2
area = lado por ancho
"""

lado = int(input("Introduce el valor del lado: "))
ancho = int(input("Introduce el valor del ancho: "))

perimetro = (lado + ancho) * 2
area = lado * ancho

print(f"El perimetro es: {perimetro}")
print(f"El area es: {area}")
