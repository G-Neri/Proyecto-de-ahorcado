import random

print("HOLA BIENVENIDO A MI JUEGO DE AHORCADO")

def palabra_aleatoria(): #Esta funcion selecciona al azar la palabra 
    palabras = [
        ["gato", "perro", "Monterrey"],
        ["Programacion", "Ahorcado", "Telefono"],
        ["Azucar", "Hipotenusa", "vector"]
    ]  
    
    fila = random.choice(palabras)  
    aleatoria = random.choice(fila) 
    return aleatoria

def tablero(secreto, adivinadas):#Esta funcion muestra las palabras adivinadas
    tablero=""                   #Al igual que tambien las oculta 
    for letra in secreto:
        if letra in adivinadas:
            tablero+=letra
        else:
            tablero+="_"
    print(tablero)
    
def jugar ():  #Esta funcion lo que hace es dar el numero de intentos
    secreto=palabra_aleatoria() #permite al jugador jugar 
    adivinadas=[]#Maneja la interaccion entre el jugador y el juego
    intentos_restantes=6
    
    while intentos_restantes > 0:
        tablero(secreto, adivinadas)
        letra=input("Intorduce una letra:").lower()
        
        if letra in adivinadas:
            print("Ya se alcanzo el limite de intentos")
            continue
        
        if letra in secreto:
            adivinadas.append(letra)
            if set(adivinadas)==set(secreto):
                print("Bien!")
                break
        
        else:
            intentos_restantes-=1
            print(f"INCORRECTO! te quedan {intentos_restantes}")
            
    if intentos_restantes==0:
        print(f"Lo siento perdiste la palabra era {secreto}")
        
        
def prueba():#Realiza el juego esta funcion sin alguna interaccion con el usuario
    secreto = "gato"
    adivinadas = ['g', 'a', 't', 'o']  
    intentos_restantes = 6

    tablero(secreto, adivinadas) 
    
    if set(adivinadas) == set(secreto):
        print("Prueba superada.") 
    else:
        print("Prueba fallida.")
        
def menu():#Esta funcion lo que hace es mostrar las opciones que tiene el codigo
    while True:#Llamando las funciones que fueron seleccionadas por el usuario
        print("\n--- MENÚ ---")
        print("1. Jugar")
        print("2. Funcion de prueba")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            jugar()
        elif opcion == '2':
            prueba()
        elif opcion == '3':
            print("¡OK QUE TENGA UN BUEN DIA!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

menu()