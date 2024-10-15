# O usuário insere uma palavra
palavra = input("Digite uma palavra: ")

# Verifica se o número de letras na palavra é par ou ímpar
quantidade_letras = len(palavra)

if quantidade_letras % 2 == 0:
    print(f"A palavra '{palavra}' tem uma quantidade par de letras.")
else:
    print(f"A palavra '{palavra}' tem uma quantidade ímpar de letras.")