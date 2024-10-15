import os
os.system('cls')

print(30*"#")
print("TAREFA 07 - FARENHEIT PARA CELSIUS")
print(30*"#" + "\n")
# O usuário insere a temperatura em farenheit
faren = float(input("Insira a temperatura em farenheit: "))
celsius = 5/9 * (faren - 32) # Tranforma-se em temperatura graus celsius 


# Imprime a temperatura convertida em celsius
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Temperatura em Celsius: {celsius:.1f} C°")