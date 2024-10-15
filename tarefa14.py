import os
import math

os.system('cls')

print(30*"#")
print("TAREFA 14 - TRIANGULO PERIMETRO E DIAGONAIS")
print(30*"#" + "\n")
# O usuário insere o valor da base e altura de um triângulo
base = int(input("Insira sua base: "))
altura = int(input("Insira sua altura: "))

area = base * altura

perimetro = 2 * (base + altura)
diag = math.sqrt(base ** 2 + altura ** 2)

# Imprime o valor da área, o perímetro e a diagonal do triângulo
print(30*"#" + "\n" + "TAREFA CONCLUIDA" + "\n" + 30*"#")
print(f"Area do triangulo: {area}\nPerimetro do triangulo: {perimetro}\nDiagonal do triangulo: {diag:.1f}")