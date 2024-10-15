import os
os.system('cls')

print(30*"#")
print("TAREFA 02 - SOMA")
print(30*"#" + "\n")
# O usuário insere 4 números inteiros
num1 = int(input("Insira seu 1º numero inteiro: "))
num2 = int(input("Insira seu 2º numero inteiro: "))
num3 = int(input("Insira seu 3º numero inteiro: "))
num4 = int(input("Insira seu 4º numero inteiro: "))

resul = num1 + num2 + num3 + num4 # É feita a soma dos quatro números para se adquirir o resultado

# Imprime o resultado dos números somados
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Resultado de todos somados: {resul}")