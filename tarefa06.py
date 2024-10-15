import os
os.system('cls')

print(30*"#")
print("TAREFA 06 - SALARIO GRATIFICACAO E IMPOSTO")
print(30*"#" + "\n")
# O usuário insere o valor do salário do funcionário
sal = float(input("Insira o salário do funcionário: "))
gratif = 50 # Valor da gratificação
imposto = sal * 0.10
salariototal = (sal + 50) - imposto

# Imprime o novo valor do salário
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Salário novo: R${salariototal}")