import os
import math

os.system('cls')

print(30*"#")
print("TAREFA 09 - HIPOTENUSA")
print(30*"#" + "\n")
# O usuário insere o valor dos catetos de um triângulo
base1 = int(input("Insira o valor do 1° cateto: "))
base2 = int(input("Insira o valor do 2° cateto: "))

# Calculo para se obter a hipotenusa
hipot = base1 ** 2 + base2 ** 2
hipot2 = math.sqrt(hipot)

# Imprime o valor da hipotenusa
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#" + "\n" + f"Valor da Hipotenusa: {hipot2:.1f}")