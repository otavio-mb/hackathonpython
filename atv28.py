import os

os.system("cls")

numeros = input("Insira os quatro números da placa do seu carro: ")
lista = [] # Lista onde iremos colocar os numeros da placa extraídos.
for i in numeros:
    lista.append(i) # Inserir numero na lista
final = int(lista[3]) # Extrair o quarto numero

# Esta tabela relacionará um mês com um numero
tabela_ipva = ["janeiro",0,"março",2,"maio",4,"julho",6,"setembro",8,"fevereiro",1,"abril",3,"junho",5,"agosto","outubro"]
mes = int(tabela_ipva.index(final) - 1) # Mes será o antecessor do elemento

# Por fim, imprimimos:
print(f"O mês de vencimento do IPVA será: {tabela_ipva[mes].capitalize()}")