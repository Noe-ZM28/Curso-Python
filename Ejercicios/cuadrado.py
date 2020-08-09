import sys

if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if (filas >= 1 or filas <= 9) and (columnas >= 1 or columnas <= 9):
        #codigo
        for f in range(filas):
            print("")
            for c in range(columnas):
                print(" * ", end='')
    else:
        print("Agumentos incorrectos xd")
        print("Ejemplo: scrip_1 [1-9] [1-9]")

else:
    print("Argumentos incorrectos")
    print("Ejemplo: scrip_1 [1-9] [1-9]")