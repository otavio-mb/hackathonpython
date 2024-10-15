# O usuário insere a escolha da operação e dois números
print(30*"*" + " Menu " + 30*"*")
print("Escolha a operação: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")

operacao = int(input("Digite o número da operação desejada: "))
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizando a operação de acordo com a escolha
if operacao == 1:
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
elif operacao == 2:
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == 3:
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não permitida.")
elif operacao == 5:
    resultado = num1 ** num2
    print(f"O resultado da potenciação é: {resultado}")
else:
    print("Operação inválida.")