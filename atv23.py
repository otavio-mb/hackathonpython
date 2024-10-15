# Função para calcular peso da pessoa
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Função para determinar o grau de obesidade da pessoa
def determinar_grau_obesidade(imc):
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc <= 24.9:
        return "Saudável"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade Grau I"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade Grau II"
    elif imc >= 40.0:
        return "Obesidade Grau III"
    else:
        return "IMC inválido"

# O usuário insere os dados 
peso = float(input("Informe seu peso em kg: "))
altura = float(input("Informe sua altura em metros: "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)

# Impressão dos resultados
print(f"Seu IMC é {imc:.2f}")
print(f"Seu grau de obesidade é: {determinar_grau_obesidade(imc)}")