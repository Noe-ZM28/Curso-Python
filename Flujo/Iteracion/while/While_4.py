while (True):
    print("*************************")
    print("**Selecciona una opcion**")
    print("*************************")
    print("""1) Saludar
2) Sumar 2 numeros
3) Salir""")
    print("<: ")
    opcion = input()

    if opcion == '1':
        print("Hola:D")
    elif opcion == '2':
        a = float(input("Ingrese un numero: "))
        b = float(input("Ingrese otro numero: "))
        print("El resultado es: " ,a+b)
    elif opcion == '3':
        print("Adios:D")
        break
    else:
        print("opcion incorrecta")
