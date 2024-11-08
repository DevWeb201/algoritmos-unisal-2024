"""Ejercicio 03
Calcular el nuevo salario del empleado por el imcremento en x%
"""

def calcular_nuevo_salario(salario, incremento):
    """
    Calcular el nuevo salario del empleado por el imcremento en x%
    """
    return salario + (salario * (incremento/100))

print(f"El nuevo salario es: ${calcular_nuevo_salario(550, 3.5):.2f} ")