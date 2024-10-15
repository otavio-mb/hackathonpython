# Faça um programa que receba dois números maiores que zero, calcule e mostre um 
# elevado ao outro.

import os

os.system('cls')

print(30*"#")
print("TAREFA 11 - NUMERO ELEVADO POR OUTRO")
print(30*"#" + "\n")

# Função aonde o usuário insere o 1° e o 2° número, logo após é feita a verificação para ver se os números inseridos são maiores que 0
def inserirnum():
    num1 = int(input("Insira seu 1° numero: "))
    num2 = int(input("Insira seu 2° numero: "))
    while True:
        if not num1 > 0 or not num2 > 0:
            print("Seus numeros tem que ser maior que zero. Tente novamente.")
            inserirnum()
        
        else: # Caso o número inserido for maior que zero, será impresso o 1° número elevado pelo 2° número
            elev = num1 ** num2
            print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Valor da elevação: {elev}")
            break

inserirnum()