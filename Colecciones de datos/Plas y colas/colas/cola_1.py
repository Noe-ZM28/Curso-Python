from collections import deque #se usa para crear una cola

cola = deque(['noe', 'brenda', 'alguien'])
cola.append('carlos xd')
cola.append('otro mas')

print(cola)

p = cola.popleft()
print(cola, p)