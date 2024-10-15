# O usuário insere a letra que deseja
letra = input("Digite uma letra: ").lower()

# Verifica se a letra inserida pelo usuário é vogal ou consoante
if letra in 'aeiou':
    print(f"A letra {letra.upper()} é uma vogal.")
elif letra.isalpha():
    print(f"A letra {letra.upper()} é uma consoante.")
else:
    print("Erro: Isso não é uma letra válida.")