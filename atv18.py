# Percurso em quilômetros e os tipos de carros
percurso = float(input("Digite o percurso da viagem em km: "))
tipo_carro = input("Digite o tipo de carro (A, B ou C): ").upper()
preco_combustivel = float(input("Digite o preço do combustível por litro (em reais): "))

# Definindo o consumo por tipo de carro
if tipo_carro == 'A':
    consumo = 16  # Carro tipo A faz 16 km/l
elif tipo_carro == 'B':
    consumo = 12  # Carro tipo B faz 12 km/l
elif tipo_carro == 'C':
    consumo = 8   # Carro tipo C faz 8 km/l
else:
    print("Tipo de carro inválido.")
    consumo = 0

# Cálculo do consumo estimado e valor da viagem
if consumo > 0:
    litros_necessarios = percurso / consumo
    custo_viagem = litros_necessarios * preco_combustivel

    print(f"\nO carro irá consumir aproximadamente {litros_necessarios:.2f} litros de combustível.")
    print(f"O valor estimado da viagem será: R$ {custo_viagem:.2f}")