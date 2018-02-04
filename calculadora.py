#Cristina del Río Vergel. 2er ejercicio: calculadora
#!/usr/bin/python3

import sys
funcion= sys.argv[1]
operando1= float(sys.argv[2])
operando2= float(sys.argv[3])
if len(sys.argv)!= 4:
	sys.exit("Argumentos inválidos. Argumentos correctos:(python3 calculadora.py funcion operando1 operando2)")
elif funcion== "sumar":
    print("El resultado de la suma es: ", operando1 + operando2)
elif funcion== "restar":
    print("El resultado de la resta es: ", operando1 - operando2)
elif funcion== "multiplicar":
    print("El resultado de la multiplicación es: ", operando1 * operando2)
elif funcion== "division":
    try:
        print("El resultado de la división es :", operando1 / operando2)
    except ZeroDivisionError:
        print ("Error, estás dividiendo entre cero")
else:
    print("NO se acepta este tipo de función, pruebe con (sumar, restar, multiplicar, dividir)") 
