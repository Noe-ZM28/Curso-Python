import sys
if len(sys.argv) == 3:
    texto = sys.argv[1]

    repetir = int(sys.argv[2])
    for r in range(repetir):
        print(texto)
else:
    print("introduce valores")