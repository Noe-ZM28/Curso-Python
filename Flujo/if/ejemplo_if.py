nota = float(input("ingresa la nota: "))

if nota >=90 and nota <= 100:
    print("muy bien")
elif nota <90 and nota > 70:
    print("apenas")

elif nota <=70 and nota >=60:
    print("insuficiente")

elif nota < 60 and nota >= 0:
    print("reprobado")

else:
    print("dato incorrecto")