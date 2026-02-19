reta = int(input('Digite o valor da primeira reta: '))               # Lê o comprimento da primeira reta
reta2 = int(input('Digite o valor da segunda reta: '))              # Lê o comprimento da segunda reta
reta3 = int(input('Digite o valor da terceira reta: '))              # Lê o comprimento da terceira reta

# Para formar um triângulo, cada lado deve ser menor que a soma dos outros dois
if reta < reta2 + reta3 and reta2 < reta + reta3 and reta3 < reta + reta2: # Condição matemática da existência de um triângulo
    print('Verdadeiro! Essas retas PODEM formar um triângulo.')       # Executa se a soma de quaisquer dois lados for maior que o terceiro
else:                                                                # Caso uma das somas seja menor ou igual ao terceiro lado
    print('Falso! Essas retas NÃO PODEM formar um triângulo.')        # Executa se for impossível fechar o triângulo com essas medidas