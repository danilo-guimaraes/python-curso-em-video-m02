salario = float(input('Digite o valor do seu salario: ').strip(' '))  # Lê o salário, limpa espaços e converte para decimal (float)
if salario >= 1250:                                                   # SE o salário for maior ou igual a R$ 1.250,00
    salarios = salario + (salario * 0.10)                             # Calcula o novo salário com aumento de 10%
    aumento = salarios - salario                                      # Calcula apenas o valor que foi somado (a diferença)
    print(f'Como seu salario é de R${salario:.2f}, seu novo salario é de R${salarios:.2f}') # Exibe os valores formatados
    print(f'O seu valor de aumento é R${aumento:.2f}')                # Mostra o valor exato do aumento recebido
else:                                                                 # SENÃO (caso o salário seja menor que R$ 1.250,00)
    salarios = salario + (salario * 0.15)                             # Calcula o novo salário com aumento maior, de 15%
    aumento = salarios - salario                                      # Calcula o valor do aumento de 15%
    print(f'Como seu salario atual é R${salario:.2f}, o seu novo salario sera de R${salarios:.2f}') # Exibe o novo salário
    print(f'O seu aumento é de R${aumento:.2f}')                     # Exibe quanto o salário subiu em reais