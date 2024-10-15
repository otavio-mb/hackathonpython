import os
os.system('cls')

print(30*"#")
print("TAREFA 03 - MEDIA DE NOTAS")
print(30*"#" + "\n")
# O usuário insere 3 notas para se calcular a média
nota1 = float(input("Insira sua 1º nota: "))
nota2 = float(input("Insira sua 2º nota: "))
nota3 = float(input("Insira sua 3º nota: "))
resul = (nota1 + nota2 + nota3) / 2 # Adquirir a média das notas

# Imprime a média das notas
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Resultado da media: {resul:.1f}")