# Pede que o usuário insira o peso da pessoa 
peso = float(input('Digite o peso atual da pessoa (em kg) :'))

# Faz a comparação com o aumento e perca de peso em relação ao dado inserido pelo usuário
peso_engordar = peso + (peso * 0.15) 
peso_emagrecer = peso - (peso * 0.20)

# Imprime a comparação adicionando e diminuindo uma taxa do peso da pessoa
peso_pessoa = print(f'\nSe a pessoa engordar seu peso será: {peso_engordar}, caso ela emagreça seu peso será: {peso_emagrecer}')