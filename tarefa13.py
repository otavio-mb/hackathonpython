import os

os.system('cls')

print(30*"#")
print("TAREFA 13 - SALARIO E HORAS TRABALHADAS")
print(30*"#" + "\n")
# O usuário insere as horas trabalhadas juntamente con o valor do salário mínimo
horastr = float(input("Insira o valor de horas trabalhadas: "))
sal_minimo = float(input("Insira o valor do salário minimo: "))
horatrab = sal_minimo / 2 
salariobruto = horastr * horatrab
imposto = salariobruto * 0.03
saltotal = salariobruto - imposto

# Imprime o valor do salário total
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Salário Total: {saltotal:.1f}")