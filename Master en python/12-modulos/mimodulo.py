
def holaMundo(nombre):
    return f"Hola que tal estás; {nombre}"
    

def calculadora (numero1, numero2, basicas = True):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = " "

    if basicas != False:
     cadena += "Suma : " + str(suma)
     cadena += "\n"
     cadena += "Resta :"  + str (resta)
     cadena += ("\n")
    else:
     cadena += "Multiplicación : " + str (multi)
     cadena += ("\n")
    cadena += "división : " + str (division)

    return cadena

    print(calculadora(56 ,5, True))
