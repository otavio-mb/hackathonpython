# O usuário insere um número inteiro entre 1 e 7
dia = int(input("Digite um número entre 1 e 7: "))

# Verifica se o número inserido pelo usuário esta dentro de algum do dia da semana
if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Não existe dia da semana com esse número.")