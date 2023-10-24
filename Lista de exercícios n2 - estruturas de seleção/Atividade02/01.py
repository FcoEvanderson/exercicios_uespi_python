quant, nome, cpf = 0, [], []

quant = int(input("Digite a quantidade de pessoas que serão hospedadas:"))
for i in quant:
    a = input("Digite o nome:")
    b = int(input("Digite o CPF:"))
    nome.append(a)
    cpf.append(b)
print(nome)
print(cpf)