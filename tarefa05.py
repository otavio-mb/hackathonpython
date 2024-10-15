import os
os.system('cls')

print(30*"#")
print("TAREFA 05 - SALARIO E PERCENTUAL")
print(30*"#" + "\n")
# O usuário insere o valor do salário do funcionário juntamente com o percentual do aumento
sal = float(input("Insira o salário do funcionário: "))
aum_perc = int(input("Insira o percentual do aumento: "))
sal_com_aumento = sal + (sal * (aum_perc/100)) # Aumento de salário com porcentual 

# Imprime o novo valor do salário com percentual pós aumento
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Salário novo pós aumento de {aum_perc}%: R${sal_com_aumento:.1f}")