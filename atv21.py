# O usuário insere os números A e B
a = int(input("Digite o número A: "))
b = int(input("Digite o número B: "))

# Verifica se o número A é divisível por B
if b != 0:
    if a % b == 0:
        print(f"{a} é divisível por {b}.")
    else:
        print(f"{a} não é divisível por {b}.")
else:
    print("Erro: Não é possível dividir por zero.")