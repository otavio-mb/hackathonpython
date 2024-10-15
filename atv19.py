# O usuário insere três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Função para encontrar o menor e o maior número
menor = min(num1, num2, num3)
maior = max(num1, num2, num3)

# Imprime a saída do menor e maior valor
print(f"O menor valor é {menor} e o maior valor é {maior}.")

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