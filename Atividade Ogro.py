from random import randint
lista = []
b = 0
while b < 10:
    a = randint(0,10)
    if a not in lista:
        lista.append(a)
        b += 1
j = 1
print(lista)
for item in lista:
    if item == 0:
        print('**')
    elif item < 6:
        print("I" * item, "*")
    else:
        print("IIIII", "I" * (item-5))