
#Variáveis do programa:
quant, i = 0, 0
nome, cpf = [], []

#Letra A:
quant = int(input("Digite a quantidade de pessoas que serão hospedadas:"))

#Letra B e C:
while i < quant:
    a = input("Digite o nome:")
    b = int(input("Digite o CPF:"))
    nome.append(a)
    cpf.append(b)
    i += 1
print(f"Quantidade de pessoas:{quant}")   
print(f"Nome:{nome}")
print(f"CPF:{cpf}")


pdt = ["tv", "iphone", "kindle", "mac", "pc", "ssd", "ipad", "memoria"]
etq = [4, 10, 8, 7, 2, 18, 5, 12]

for i in etq:
    if etq[i] < 5:
        etq.remove(i)
        print(f"Produtos = {pdt}")
        print(f"Estoque = {etq}")
    else:
        print(f"Produtos = {pdt}")
        print(f"Estoque = {etq}")