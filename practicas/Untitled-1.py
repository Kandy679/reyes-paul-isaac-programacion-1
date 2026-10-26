## Ejercicio 1 Clasificación por edad ##
"""
edad = int(input("Introduzca su edad para comprobar su clasificación de edad:"))
if edad < 13:
    print("Usted entra en la clasificación de niños")
elif edad < 18:
    print("Usted entra en la clasificación de adolescentes")
else:
    print("Usted entra en la clasificación de adultos")

## Ejercicio 2 Validar acceso ##
usuario = input("Crea un nombre de usuario:")
contraseña = input("Crea una contraseña:")

info = input("Usuario:")
info2 = input("Contraseña:")

if info == usuario and info2 == contraseña:
    print("¡Sesión iniciada exitosamente!")
else:
    print("Compruebe su usuario o contraseña e intentelo de nuevo")

    """


## Ejercicio 3 Calculadora de envio ##

print("¡El día de hoy contamos con un 10% de descuento en productos que sobrepasen los 10kg de peso!:")
peso = int(input("Especifique el peso en kilogramos de su producto para calcular el costo de envio:"))

if peso == 1:
    print("El costo de envio será de $50 pesos")
elif peso <= 5:
    print("El costo de envio será de $90 pesos")
elif peso > 5:
    print("El costo de envio será de 150 pesos")
elif peso > 10:
    print("Su envio cuenta con un 10% de descuento")

## Ejercicio 
