"""Cristina del Río Vergel.
Ejercico 2 de python: Hacer una calculadora!/usr/bin/"""
import sys
# extracción de argumentos
try:
    funcion = sys.argv[1]
    operando1 = float(sys.argv[2])
    operando2 = float(sys.argv[3])
except ValueError:
    sys.exit("Error, sólo puedes meter operandos que sean números.")
# control de argumentos
if len(sys.argv) != 4:
    sys.exit("Argum inval:python3 calculadora.py funcion operando1 operando2")
elif funcion == "sumar":
    print("El resultado de la suma es: ", operando1 + operando2)
elif funcion == "restar":
    print("El resultado de la resta es: ", operando1 - operando2)
elif funcion == "multiplicar":
    print("El resultado de la multiplicación es: ", operando1 * operando2)
elif funcion == "division":
    try:
        print("El resultado de la división es: ", operando1 / operando2)
    except ZeroDivisionError:
        print("Error, estás dividiendo entre cero")
else:
    print("NO aceptable,pruebe con(sumar, restar, multiplicar, dividir)")
