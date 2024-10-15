import os
os.system('cls')
print(30*"#")
print("TAREFA 01 - ANTECESSOR E SUCESSOR")
print(30*"#" + "\n")
# O usuário insere um número inteiro
num = int(input("Insira seu numero inteiro: "))
ant = num - 1 # Adquirir o antecessor
suc = num + 1 # Adquirir o sucessor

# Impressão do antecessor e sucessor do número inserido pelo usuário
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Antecessor: {ant}" + "\n" + f"Sucessor: {suc}")