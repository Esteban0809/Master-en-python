"""
Ejercicio 6 . Mostrar todas las tablas de multiplicar del 1 al 10,
mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
"""

for cabecera in range (1, 11):

    print("###############################")

    print(f"########### La Tabla Del {cabecera}  ##############")
    for numero in range (1, 11):
        print(f"{numero} x {cabecera} = {numero*cabecera}")

    print("\n")