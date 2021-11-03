'''
Faça um programa insira em um dicionário vários nomes de pessoas e respectivas
idades. APENAS DEPOIS que tiver inserido todos os dados no dicionário, criar
uma lista com o nome das pessoas com k acima de 30 anos e outra lista com o
nome das pessoas com k abaixo de 30 anos.
'''
#Criando as listas de k e nome, e um dicionario.
nomes = []
idades = []
dados=dict()

'''Adicionando dados as listas, e depois adicionando estes dados ao dicionario'''
for k in range(4):
    n = input('Informe o nome: ')
    i = int(input('informe a idade: '))
    nomes.append(n)
    idades.append(i)
    dados[nomes[k]]=idades[k]

'''Listas para adicionar o nome das pessoas com mais, menos, exatamente igual a 30 anos'''
maior=[]
menor=[]
exato=[]

'''Percorrendo o dicionario. Usa .key() para percorrer os nomes(key) do dicionario,
e para cada key, ele vai procurar o value'''
for k in dados.keys():
    if dados[k] > 30 :
        maior.append(k)
    elif dados[k] < 30:
        menor.append(k)
    #para o caso de ter exatamente 30 anos (não explicitado na questão)
    else:
        exato.append(k)

print('Maior de 30 anos: ', maior)
print('Menor de 30 anos: ', menor)

#Só imprime se houver alguem com exatamente 30 anos
if exato != []:
    print('Exatamente 30 anos: ',exato)