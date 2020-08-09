import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero <= 9999 and numero >= 0:
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print("{:04d}".format(int(cadena[longitud-1-i]) * 10 ** i ))

    else:
        print("Argumento invalido")
        print("ejemplo: descomposicion.py [0 - 9999]")
else:
    print("Argumento invalido")
    print("ejemplo: descomposicion.py [0 - 9999]")