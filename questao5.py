# Define a string a ser invertida
string = "Exemplo de string a ser invertida"

# Converte a string para uma lista de caracteres
caracteres = list(string)

# Define os índices inicial e final da lista
i = 0
j = len(caracteres) - 1

# Percorre a lista invertendo os caracteres
while i < j:
    # Troca os valores dos índices i e j
    temp = caracteres[i]
    caracteres[i] = caracteres[j]
    caracteres[j] = temp

    # Incrementa o índice i e decrementa o índice j
    i += 1
    j -= 1

# Converte a lista de caracteres de volta para uma string
string_invertida = ''.join(caracteres)

# Exibe a string invertida na tela
print(string_invertida)
