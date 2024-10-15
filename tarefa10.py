import os
import math

os.system('cls')

print(30*"#")
print("TAREFA 10 - NUMERO VARIACOES")
print(30*"#" + "\n")
# O usuário insere um número 
num = int(input("Insira seu número: "))

quad = num ** 2 # O número é elevado ao quadrado
cubo = num ** 3 # O número é elevado ao cubo
raizquad = math.sqrt(num) # Se obtem a raiz quadrada do número inserido pelo usuário
raizcubo = math.cbrt(num) # Se obtem a raiz cúbica do número inserido pelo usuário

# Imprime as resoluções dos cálculos 
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#")
print(f"{num} ao quadrado: {quad}")
print(f"{num} ao cubo: {cubo}")
print(f"Raiz quadrada de {num}: {raizquad:.1f}")
print(f"Raiz cubica de {num}: {raizcubo:.1f}")