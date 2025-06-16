import random

def mostrar_estado(palabra_secreta, letras_adivinadas, letras_fallidas, intentos_restantes):
    palabra_mostrada = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            palabra_mostrada += letra + ' '
        else:
            palabra_mostrada += '_ '
    print("\nPalabra:", palabra_mostrada)
    print("Letras fallidas:", ' '.join(letras_fallidas))
    print("Intentos restantes:", intentos_restantes)

def jugar_ahorcado():
    palabras = ["python", "ahorcado", "colab", "programacion", "computadora"]
    palabra = random.choice(palabras)
    letras_adivinadas = []
    letras_fallidas = []
    intentos = 8
    estado = "En curso"

    print("🎮 Bienvenido al juego del Ahorcado 🎮")
    print("Pista: la palabra tiene", len(palabra), "letras.")

    while estado == "En curso":
        mostrar_estado(palabra, letras_adivinadas, letras_fallidas, intentos)
        letra = input("Introduce una letra: ").lower()

        if letra in letras_adivinadas or letra in letras_fallidas:
            print("⚠️ Ya ingresaste esa letra.")
            continue

        if letra in palabra:
            letras_adivinadas.append(letra)
            if all(l in letras_adivinadas for l in set(palabra)):
                estado = "Ganado"
        else:
            intentos -= 1
            letras_fallidas.append(letra)
            if intentos == 0:
                estado = "Perdido"

    if estado == "Ganado":
        print("\n🎉 ¡Felicidades! Has adivinado la palabra:", palabra)
    else:
        print("\n💀 Has perdido. La palabra era:", palabra)

    jugar_nuevamente = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if jugar_nuevamente == 's':
        jugar_ahorcado()
    else:
        print("Gracias por jugar. ¡Hasta pronto!")

# Iniciar juego
jugar_ahorcado()
