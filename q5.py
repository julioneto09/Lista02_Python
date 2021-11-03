'''
Faça um Programa que leia duas listas com 15 elementos cada e gere uma terceira
lista formada pelos elementos intercalados das duas outras listas. O programa deve
exibir a quantidade de elementos de cada lista, bem como seus elementos.
'''
#Importando a biblioteca random para gerar numeros aleatorios
import random

n = 15

l1=[]
l2=[]

'''criando as listas l1 e l2 com numeros inteiros aleatórios (preguiça de digitar 15 termos diferentes, 
2 vezes)
random.randint() gera numeros inteiros aleatorios entre 0 e 20 [0,20)
random.random() gera numeros flutuantes aleatorios entre 0 e 1 [0,1)
round(x,y) arredonda os termos x com y casas decimais (já que x é float)'''
for k in range(n):
    l1.append(random.randint(0,20))
    l2.append(round(random.random(),2))

'''a lista l3 vai receber os termos das listas l1 e l2.
Foi usado o método .extend() para que cada termo seja adicionado individualmente.'''
l3 = []
for c in range(n):
    l3.extend((l1[c],l2[c]))
print(l3)

print(f'\nLista 1: {l1}')
print(f'Comprimento da lista 1: {len(l1)}')
print(f'\nLista 2: {l2}')
print(f'Comprimento da lista 2: {len(l2)}')
print(f'\nLista 3: {l3}')
print(f'Comprimento da lista 3: {len(l3)}')
