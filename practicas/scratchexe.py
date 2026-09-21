import time
import random

def programa_scratch():
    # when green flag clicked
    print("¡Hola!")
    time.sleep(2)

    # ask "¿Cómo te llamas?" and wait
    nombre = input("¿Cómo te llamas? ")
    print(f"Hola, {nombre}")
    time.sleep(1)

    # ask "¿Cuantos años tienes?" and wait
    edad = input("¿Cuantos años tienes? ")

    # if answer < 15 then / else
    try:
        edad_num = float(edad)
    except ValueError:
        edad_num = 0

    if edad_num < 15:
        print("Activa cam")
    else:
        print("Ya estas bien grande")

    time.sleep(1)

    # repeat 25: turn 15 degrees
    direccion = 90  # dirección inicial típica en Scratch
    for _ in range(25):
        direccion += 15
        # En un motor gráfico real, aquí rotarías el sprite:
        # sprite.rotate(15)
    print(f"(El sprite giró hasta quedar apuntando a {direccion % 360}°)")

    time.sleep(1)

    # ask "¿Wachaste ese backflip?" and wait
    respuesta_backflip = input("¿Wachaste ese backflip? ")

    # set "mi variable" to 0
    mi_variable = 0

    # if answer = "Si" then / else
    if respuesta_backflip.strip().lower() == "si":
        print("Yippie!! :D")
    else:
        print("Te voy a matar")

    time.sleep(1)

    # switch costume to costume1
    disfraz_actual = "costume1"
    # sprite.set_costume(disfraz_actual)

    time.sleep(0.5)

    # set volume to 100000000 %
    volumen = 100000000
    # sprite.set_volume(volumen)  # Nota: Scratch limita esto internamente a 100%

    # start sound "Miau"
    # sprite.play_sound("Miau")
    print("🔊 (reproduciendo sonido: Miau)")

    # change size by 1000000
    tamaño = 100 + 1000000  # tamaño inicial (100%) + el cambio
    # sprite.set_size(tamaño)
    print(f"(El sprite ahora mide {tamaño}% de su tamaño original)")


if __name__ == "__main__":
    programa_scratch()
