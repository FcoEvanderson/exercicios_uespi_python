a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

if a > b:
    print(f"{a} é maior do que {b}.")
elif a == b:
    print("Esses números tem o mesmo valor.")
else:
    print(f"{b} é maior do que {a}.")

c = int(input("Digite um número: "))
d = int(input("Digite outro número: "))

if c > d:
    print(f"{d} é menor que {c}.")
elif c == d:
    print("Esses números tem o mesmo valor.")
else:
    print(f"{c} é menor que {d}.")