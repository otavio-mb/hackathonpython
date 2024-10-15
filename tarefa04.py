import os
os.system('cls')

print(30*"#")
print("TAREFA 04 - SALARIO")
print(30*"#" + "\n")
# O usuário insere o valor do salário do funcionário
sal = float(input("Insira o salário do funcionário: "))
sal_com_aumento = sal + (sal * 25/100) # 25/100 = 0.25, calculamos o aumento que haverá no salário

# Imprime o novo valor do salário pós aumento
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Salário novo pós aumento de 25%: R${sal_com_aumento:.1f}")