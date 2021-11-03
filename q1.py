'''
Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. 
O programa deve perguntar o valor da casa a comprar, o salário e quantidade de anos a pagar. 
O valor da prestação mensal não pode ser superior a 30% do salário. 
Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
'''

def converter(x):
    '''Converter a quantidade de anos (x) em meses'''
    mes = x*12
    return(mes)

def maximo(y):
    '''Dado o salário (y), determinar o valor máximo da prestação mensal'''
    lim = y*0.3
    return(lim)

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos você pagará a casa? '))

meses = converter(anos)
limite = maximo(salario)

prestação = valor/meses

v = meses*limite

if prestação < limite :
    print('\nParabéns! Você tem crédito aprovado para a compra da casa.')
else: 
    print('\nVocê tem crédito para comprar uma casa de até R$ ',v)
