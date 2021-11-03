'''
Mostre como converter:
a. Chaves do dicionário em uma lista
b. Valores do dicionário em uma lista
c. Dicionário em uma lista de tuplas, cujos elementos são as chaves e os valores
'''

chave=[]
valor=[]
dados = {'chave1': 1, 'chave2': 2, 'chave3': 3, 'chave4': 4}
for key,value in dados.items():
    chave.append(key)
    valor.append(value)

print('As chaves: ',chave)
print('Os valores: ',valor)

