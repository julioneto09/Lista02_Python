'''
Escreva um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
• "Telefonou para a vítima?"
• "Esteve no local do crime?"
• "Mora perto da vítima?"
• "Devia para a vítima?"
• "Já trabalhou com a vítima?"
No final o programa deve imprimir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso krário, ele será classificado como "Inocente".
'''
perguntas = ['Telefonou para a vítima? ', 'Esteve no local do crime? ', 'Mora perto da vítima? ', 
'Devia para a vítima? ', 'Já trabalhou com a vítima? ']

#Uma lista (r) para as respostas, e outra lista (q) com 5 items, vai receber as 5 perguntas
r=[]
q = ['a','b','c','d','e']

for k in range(5) :
    while True:
        q[k] = input(perguntas[k])
        if  (q[k] =='sim') or (q[k]=='não'):
            break
        else:
            print("Favor, digitar 'sim' ou 'não'")
        #if-else verifica se o usuario respondeu corretamente a pergunta
    r.append(q[k])
    #r recebe as respostas das perguntas

s = r.count('sim')
#o método .count irá contar quantas vezes o termo 'sim' está presente em r

#O usuário é classificado conforme a quantidade de 'sim' presente nas respostas
if s == 5 :
    print('\nAssassino(a)!!!')
elif s > 2 :
    print('\nCúmplice!')
elif s == 2:
    print('\nSuspeito(a).')
else: 
    print('\nInocente.')
