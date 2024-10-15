import os

os.system('cls')

print(30*"#")
print("TAREFA 15 - PRESTAÇÃO EM ATRASO")
print(30*"#" + "\n")
# O usuário insere o valor da prestação inicial, da taxa de juros e o tempo de atraso em dias
presta_ini = float(input("Insira o valor da prestação inicial: "))
taxajur = float(input("Insira o valor da taxa de juros: "))
tempatraso = float(input("Insira o valor do tempo de atraso em dias: "))

presta_fin = presta_ini + presta_ini * (taxajur / 100) * tempatraso

# Imprime o valor da prestação em atraso final
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Prestação em atraso final: {presta_fin:.1f}")