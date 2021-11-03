'''
Escreva um programa que carregue uma lista com os modelos de dez carros (Fusca, Gol,
Celta, Uno, etc) e outra lista com o consumo de cada modelo (km/litro). Por fim, exiba:
a. O modelo do carro mais econômico.
b. Quantos litros cada modelo de carro cadastrado consome para percorrer uma
distância de X km.
c. Quanto será gasto de combustível para percorrer X km, considerando que a
gasolina custe R$ 5,50 o litro.
'''

modelos = ['Hb20','Onix','Argo','Kwid','Hilux','Fox','Uno','Gol','Corolla','Compass']
consumo = [9.8, 13.0, 12.0, 15.0, 8.0, 9.5, 11.5, 10.0, 9.0, 9.0]

valor = 5.5 #onde está esse preço?

#Criando uma só lista, onde cada elemento dela tem o modelo e seu respectivo consumo
carros = []
for a in range(len(modelos)):
    carros.append((consumo[a],modelos[a]))

'''O método .sort() ordena a lista de forma crescente (por isso, ao criar a lista 'carros', 
o primeiro argumento foi o consumo).
Já o método max() informa qual o maior item da lista. No nosso caso, buscamos o que tem a maior relação
km/l'''
carros.sort()
m=max(carros)

x=float(input('Informe quantos quilometros que deseja percorrer: '))

litros=[]
custo=[]

print(f'\na) O modelo mais economico é: {m[1]}, com média de {m[0]} km/L')

'''Para determinar quantos litros o carro consumiu, divide-se a distância pela relação km/l
Já para o custo, multiplica-se a quantidade de litros consumidos pelo valor da gasolina'''
for k in range(len(modelos)):
    litros.append(x / carros[k][0])
    custo.append(valor*litros[k])
    print(f'\nCarro: {carros[k][1]}, consumo: {litros[k]:.2f} L, custo: R$ {custo[k]:.2f}')
