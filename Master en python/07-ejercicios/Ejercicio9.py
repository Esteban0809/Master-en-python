"""
Ejercicio 9 Hacer un programa que pida numeros al usaurio
indefinidamente hasta meter el 111
"""
contador = 1
while contador <100:
    numero = int(input(" Introduce un numero  :" ))

    if numero == 111:
        break
    else:
        print (f"has introducido el {numero}")