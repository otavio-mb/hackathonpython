import os
os.system('cls')

print(30*"#")
print("TAREFA 08 - AREA DE TRIANGULO")
print(30*"#" + "\n")
# O usuário insere o valor da base e altura de um triângulo
base = int(input("Insira a base de seu triangulo: "))
alt = int(input("Insira a altura do mesmo: "))
area = (base * alt) / 2 # Calcula-se a área desse triângulo

# Imprime a área do triângulo
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Area do triangulo: {area}")