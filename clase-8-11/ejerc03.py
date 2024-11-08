"""Ejercicio 03
Calcular el nuevo salario del empleado por el imcremento en x%
"""

def calcular_nuevo_salario(salario, incremento):
    """
    Calcular el nuevo salario del empleado por el imcremento en x%
    """
    return salario + (salario * (incremento/100))

salario = 550
incre = 3.5
print(f"El salario anterior es: ${salario:.2f} ")
print(f"Elm incremento es de {incre}%")
print(f"El nuevo salario es: ${calcular_nuevo_salario(salario, 3.5):.2f} ")