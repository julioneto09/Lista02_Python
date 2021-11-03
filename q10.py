'''
Crie um programa que exiba uma listagem de preços de produtos em forma tabular.
Utilize uma tupla única com nomes e preços dos produtos.
'''

'''Notas:
Essa questão podia ser resolvida usando from tabulate import tabulate, mas não consegui
compreender a sintaxe/uso dele, então fiz a tabela na "mão"
'''

#Lista de Produtos
produtos=('Hb20',55000,'Onix',58000,'Argo',52000,'Kwid',48000,
'Hilux',210000,'Fox',60000,'Uno',49000,'Gol',51000,'Corolla',100000,'Compass',110000)

#Impimir o cabeçalho da tabelha
print ('\n{:<8} {:<15}\n'.format('Modelo','Valor (R$)'))

'''Imprimir os dados
o range() está com passo 2, pois salvei a tupla no formato modelo-preço, logo, para imprimir
cada modelo(e respectivo preço) em cada linha, tem que passar de 2 em 2 itens
'''
for k in range(0,len(produtos),2):
    print ('{:<8} {:<15}\n'.format(produtos[k], produtos[k+1]))
    

