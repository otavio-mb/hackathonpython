import os

os.system('cls')

print(30*"#")
print("TAREFA 12 - PÉS, JARDAS E MILHAS")
print(30*"#" + "\n")

# O usuário insere a medida em pés
pe = int(input("Insira sua medida em pés: "))
polegada = pe * 12 # Resolução da medida de pés em polegada 
jarda = pe * 3  # Resolução da medida de pés em jarda 
milha = 1.760 * jarda # Resolução da medida de jarda em milha

# Imprime a medida de pés em polegadas, jardas e milhas
print("\n" + 30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#")
print(f"Polegadas: {polegada:.1f}\nJardas: {jarda:.1f}\nMilhas: {milha:.1f}")
print(30*"#" + "\n")