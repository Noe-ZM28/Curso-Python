#Son arreglos, pero con cualquier tipo de dato que le quiera poner

numeros = [1, "dos", 'tres', 4.0]
print(numeros)


# la funcion .append me prmite agregar un nuevo dato a la lista al final
numeros.append(5.55555555555555)
print(numeros)


#se pueden crear listas dentro de listas
a = [0, 2, 5]
b = [".", 8, 77]

r = [a, b]
print(r)

#las listas anidadas funcionan como matrices
print(r[1][2])