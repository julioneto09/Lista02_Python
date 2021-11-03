'''
Faça um programa que solicite a idade, nome, peso e altura dos alunos de uma academia
e armazene em uma variável composta. Cada elemento da variável composta deverá
representar as características de cada aluno.
a. O programa deve permitir que o usuário pesquise o nome do aluno e como
retorno o programa deverá fornecer se o aluno está obeso ou não (faça uma
calculadora de Índice de Massa Corporal- IMC).
b. Exiba uma lista ordenada com os nomes dos alunos cadastrados. (Deixe 5 alunos
cadastrados).
c. Exiba o nome e o IMC do aluno mais pesado e do aluno mais leve.
'''

def imc(peso, altura):
    '''Dado o peso e a altura, a função calcula o IMC (peso/altura**2)
    e informa o grau de obesidade da pessoa'''
    x = peso/pow(altura,2)
    if x < 18.5:
        print('Abaixo do peso')
    elif x < 25:
        print('Peso normal')
    elif x< 30:
        print('sobrepeso')
    elif x < 35:
        print('Obesidade grau 1')
    elif x < 40:
        print('Obesidade grau 2')
    else:
        print('Obesidade grau 3')  

    return x


nome=[]
idade=[]
peso=[]
altura=[]

#imc=[]
for k in range(2):
    n = input('informe o nome: ')
    i = int(input('informe a idade: '))
    p = float(input('informe o peso: '))
    a = float(input('informe a altura: '))
    nome.append(n)
    idade.append(i)
    peso.append(p)
    altura.append(a)

id=[]
pe=[]
al=[]

aluno=[]
for k in range(1):
    x = imc(peso[k],altura[k])
    aluno.append((nome[k],idade[k],peso[k],altura[k], x))

print(aluno)
busca = input('Informe o nome do aluno: ')

#Falta completar a questão
