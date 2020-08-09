#formateo de numeros enteros, rellenados con espacios

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

#formateo de numeros enteros, rellenados con ceros
print("")
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#formateo de numeros flotantes, solo n cantidad de decimales
print("")
print("{:.2f}".format(3.14159))
print("{:.3f}".format(3.14159))
print("{:.4f}".format(3.14159))

#formateo de numeros flotantes, alineando por la cantidad de caracteres
print("")
print("{:7.3f}".format(3.14159))
print("{:7.3f}".format(333.141))

#formateo de numeros flotantes, alineando por la cantidad de caracteres y rellenando con ceros
print("")
print("{:07.3f}".format(3.14159))
print("{:07.3f}".format(333.14))