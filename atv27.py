from datetime import datetime, timedelta
import os
# O usuário insere o nome do livro, tipo de usuário e data do empréstimo
nome_livro = input("Digite o nome do livro: ")
tipo_usuario = input("Digite o tipo de usuário (professor ou aluno): ").lower()
data_emprestimo_str = input("Digite a data de empréstimo (dd/mm/aaaa): ")

# Conversão da data de empréstimo para o formato de data
data_emprestimo = datetime.strptime(data_emprestimo_str, "%d/%m/%Y")

# Definindo o prazo de devolução
if tipo_usuario == "professor":
    prazo = 20  # Prazo para professores
elif tipo_usuario == "aluno":
    prazo = 15  # Prazo para alunos
else:
    print("Tipo de usuário inválido.")
    prazo = 0

# Calculando a data de devolução
if prazo > 0:
    data_devolucao = data_emprestimo + timedelta(days=prazo)

    # Exibindo o recibo
    os.system("cls")
    print("\n" + 10*"*" + " Recibo de Empréstimo " + 10*"*")
    print(f"Nome do livro: {nome_livro}")
    print(f"Tipo de usuário: {tipo_usuario.capitalize()}")
    print(f"Data do empréstimo: {data_emprestimo_str}")
    print(f"Data da devolução: {data_devolucao.strftime('%d/%m/%Y')}")
    print (42*"*")