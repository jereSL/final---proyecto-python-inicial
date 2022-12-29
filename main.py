import csv
import random
import interfaz


def leer_palabra_secreta(csvfilename):
    archivo = 'palabras.csv'
    with open(archivo) as f:
        palabras_secretas = csv.DictReader(f)
        lista = list(palabras_secretas)
        lista_palabras = []
        for row in lista:
            lista_palabras.append(row['palabras'])


    palabra_secreta = random.choice(lista_palabras)
    return(palabra_secreta)

def pedir_letra(letras_usadas):
    while True:
        letra_ingresada = str(input('PULSE LETRA: '))
        letra = letra_ingresada.lower()
        if len(letra) > 1:
            continue
        else:
            if letra in letras_usadas:
                continue

            else:
                letras_usadas.append(letra)
        return(letra)
        break

def verificar_letra(letra, palabra_secreta):

    if letra in palabra_secreta:
        return(True)
    else:
        return(False)


def validar_palabra(letras_usadas, palabra_secreta):
    a = 0
    for i in palabra_secreta:
        if i not in letras_usadas:
            a = 0
        else:
            a = a + 1
    if a == len(palabra_secreta):
        return(True)
    else:
        return(False)


if __name__ == "__main__":

    print("JUEGO DEL AHORCADO")
    cantidad_intentos_total = 8
    intentos = 0
    letras_usadas = []
    ganador = False

    palabra_secreta = leer_palabra_secreta('palabras.csv')

    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

    while intentos < cantidad_intentos_total and not ganador:

        letra = pedir_letra(letras_usadas)

        if verificar_letra(letra, palabra_secreta) ==  False:
            intentos += 1

        interfaz.dibujar (palabra_secreta, letras_usadas, intentos)
        
        if validar_palabra(letras_usadas, palabra_secreta) == True:

            ganador = True
            break

    if ganador:
        print('ENHORABUENA, RESOLVISTE EL AHORCADO')
    else:
        print('FALLASTE')
       


