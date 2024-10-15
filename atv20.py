# O usuário insere um número
num = int(input("Digite um número inteiro: "))

# Verifica se o número inserido pelo usuário é múltiplo de 3
if num % 3 == 0:
    print(f"O número {num} é múltiplo de 3.")
else:
    print(f"O número {num} não é múltiplo de 3.")