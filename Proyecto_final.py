import os
import random

print("HOLA BIENVENIDO A MI JUEGO DE AHORCADO")

def crear_archivos_de_pistas(nombre_carpeta, palabras_y_pistas):
    # Crear la carpeta si no existe
    if not os.path.exists(nombre_carpeta):
        os.makedirs(nombre_carpeta)

    # Crear un archivo para cada palabra con su pista correspondiente
    for palabra, pista in palabras_y_pistas.items():
        ruta_archivo = os.path.join(nombre_carpeta, f"{palabra}.txt")
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(f"Pista: {pista}\nPalabra: {palabra}")

    print(f"Archivos de pistas creados en la carpeta '{nombre_carpeta}'.")

def palabra_aleatoria(palabras_y_pistas):
    # Seleccionar al azar una palabra y su pista
    palabra, pista = random.choice(list(palabras_y_pistas.items()))
    return palabra, pista

def tablero(secreto, adivinadas):
    tablero = ""
    for letra in secreto:
        if letra in adivinadas:
            tablero += letra
        else:
            tablero += "_"
    print(tablero)

def jugar(palabras_y_pistas):
    # Elegir una palabra y pista al azar
    secreto, pista = palabra_aleatoria(palabras_y_pistas)
    adivinadas = set()
    letras_incorrectas = set()
    intentos_restantes = 6
    pista_usada = False

    while intentos_restantes > 0:
        tablero(secreto, adivinadas)
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras incorrectas: {', '.join(letras_incorrectas)}")
        opcion = input("Introduce una letra o escribe 'pista' para obtener una pista (te costará un intento): ").lower()

        if opcion == 'pista':
            if not pista_usada:
                print(f"Pista: {pista}")
                pista_usada = True
                intentos_restantes -= 1  # Penalización por usar la pista
            else:
                print("Ya has usado la pista.")
            continue

        # Validar la entrada
        if len(opcion) != 1 or not opcion.isalpha():
            print("Por favor, introduce solo una letra.")
            continue

        letra = opcion.lower()

        if letra in adivinadas or letra in letras_incorrectas:
            print("Ya intentaste esa letra. Prueba con otra.")
            continue

        if letra in secreto.lower():
            adivinadas.add(letra)  # Agregar la letra a las adivinadas correctas
            # Comprobar si todas las letras de la palabra han sido adivinadas
            if all(l in adivinadas for l in secreto.lower()):
                tablero(secreto, adivinadas)
                print("¡Bien! ¡Adivinaste la palabra!")
                break
        else:
            letras_incorrectas.add(letra)  # Registrar la letra incorrecta
            intentos_restantes -= 1
            print(f"¡Incorrecto! Te quedan {intentos_restantes} intentos.")

    if intentos_restantes == 0:
        print(f"Lo siento, perdiste. La palabra era '{secreto}'.")

def prueba():
    secreto = "gato"
    adivinadas = ['g', 'a', 't', 'o']
    intentos_restantes = 6

    tablero(secreto, adivinadas)

    if set(adivinadas) == set(secreto):
        print("Prueba superada.")
    else:
        print("Prueba fallida.")

def menu():
    palabras_y_pistas = {
        "gato": "Animal con bigotes.",
        "perro": "Mejor amigo del hombre.",
        "Monterrey": "Ciudad en el norte de México.",
        "Programacion": "Proceso de escribir código.",
        "Ahorcado": "Juego donde adivinas palabras.",
        "Telefono": "Es para hacer llamadas.",
        "Azucar": "Es dulce y se usa en postres.",
        "Hipotenusa": "Lado opuesto al ángulo recto en un triángulo.",
        "vector": "Cantidad con magnitud y dirección."
    }

    # Crear archivos de pistas
    crear_archivos_de_pistas("Pistas", palabras_y_pistas)

    while True:
        print("\n--- MENÚ ---")
        print("1. Jugar")
        print("2. Función de prueba")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            jugar(palabras_y_pistas)
        elif opcion == '2':
            prueba()
        elif opcion == '3':
            print("¡OK, QUE TENGAS UN BUEN DÍA!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()

