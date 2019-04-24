# print('Olá Mundo')

# nota1 = float(input('Me informe sua primeira nota?'))
# nota2 = float(input('Me informe sua primeira nota?'))
# nota3 = float (input('Me informe sua primeira nota?')) 

# media = (nota1 + nota2 + nota3) / 3.0

# print('Sua média foi de {}'.format (round(media))
# if media==10.0: 
#    print('aprovado, parabéns')
# elif media >= 6.0:
#     print('passou raspando')
# else: 
#     print('Pegou DP')
#---------------------------------------------------------------------------
# tempoC=int(input('Qual a temperatura em Celsius que deseja converter em  '))
# tempoF=float(tempoC *(9/5)) +32 
# print(f'{tempoC}em celsius equivalem a {tempoF} em f')
#----------------------------------------------------------------------------
# import math // para fazer contas

# exponencial= math.exp(3)

# print(exponencial)
#-----------------------------------------------------------------------------
# def calcular_pagamento(qtd_horas, valor_horas):
#     horas=float(qtd_horas)
#     dinheiro= float(valor_horas)
#     if horas >= 40: 
#         salario = horas * dinheiro
#         return salario
#     else:
#         print('você não trabalhou o suficiente')

# salario = calcular_pagamento(35, 43.6)
# print(salario)
#-------------------------------------------------------------------------------
#detetive 

# print('detetive')
# print('responda as perguntas abaixo com S(sim) ou N(não):')

# perguntas=( 'vc telefonou para a vitima', 
#             'vc esteve no local do crime?',
#             'vc era vizinha da vitima?', 
#             'vc tinha um crush na vitima?', 
#             'vc é o mordomo?'
#             'vc devia dinheiro para vitima?')

# respostas=[]

# for pergunta in perguntas: 
#     respostas.append(input(pergunta).upper())

# tipo=0 
# for resposta in respostas: 
#     if resposta == 'S':
#        tipo +=1 
# if tipo < 2: 
#     print('inocente')
# elif tipo == 2: 
#     print('acho que voce matou')
# elif tipo<= 4:
#     print('você deve ter participado do assassinato')
# else: 
#     print('você é o mordomo então você morreu')
#----------------------------------------------------------------------------------------

#Criar uma funçao de soma

# Será que a nossa turma é turma jovem
# Pergunte a idade mental dos colegas, qual a quantidade dos colegas e veja se a turma é jovem.  

#se for igual ou menos de 25 são jovens
#se for de 25 a 60 vc é idoso 
#se for mais de 60, vc é bem idoso 

# def soma(valor1,valor2): 
#     return valor1+ valor2 

# valor1= int(input('Informe o valor: '))
# valor2=int(input('Informe o valor: '))

# print(f'A soma dos valores e {soma(valor1, valor2)}')