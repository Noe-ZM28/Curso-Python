t = "Hola, soy un texto"
n = 0


#print(texto, n)

s = "un texto {0} y un numero {1}".format(t, n)
print(s)

s = "un texto {1} y un numero {0}".format(t, n)
print(s)

s = "un texto {t} y un numero {n}".format(t=t, n = n)
print(s)