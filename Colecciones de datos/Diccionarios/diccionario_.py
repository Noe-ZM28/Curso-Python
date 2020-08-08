
personajes = []

p = {'nombre':'miku uwu', 'clase':'cantante virtual', 'edad':'ni idea'}
personajes.append(p)
p = {'nombre':'kaito owo', 'clase':'cantante virtual', 'edad':'25'}
personajes.append(p)
p = {'nombre':'gummi nwn', 'clase':'cantante virtual', 'edad':'15'}
personajes.append(p)

print(personajes)

for p in personajes:
    print(p['nombre'], p['clase'], p['edad'])
