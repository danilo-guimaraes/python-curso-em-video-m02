nome = input('Qual o seu nome completo?\n').strip()
print(nome.upper()) # Exibe o nome todo em maiúsculas
print(nome.lower()) # Exibe o nome todo em minúsculas
letra = len("".join(nome.split())) # Junta as palavras sem espaços e conta o total de letras
print('Seu nome tem {} letras'.format(letra))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))