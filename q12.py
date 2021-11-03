'''
Crie um exercício que precise fazer uso da variável composta “conjunto”.
'''
#Enunciado da questão criada
print('\n\tFaça duas listas de números inteiros, e como saida, informe quais números estão presentes nas duas listas\n')

#Função criada para adicionar itens num conjunto
def add(x,y):
    y.add(x)
    return add

#Criando conjuntos, set(), vazios
l1= set()
l2 = set()

a=0
b=0

print('(Para encerrar, digite "99")\n')
#Condição para para o aplicativo
while a != 99:
    a =int(input('Informe um número para a lista 1: '))
    '''esse if-else garante que o numero 99 (condição para encerrar o aplicativo) 
    não vai ser adicionado ao conjunto'''
    if a != 99:
        add(a, l1)
    else:
        print('\n')

while b != 99:
    b =int(input('Informe um número para a lista 2: '))
    if b != 99:
        add(b, l2)
    else:
        print('\n')

'''Essa operação faz a interseção dos conjuntos. Podia ser substituida por: 
l3 = l1.intersection(l2)
'''
l3 = l1 & l2
if l3 == set():
    print('As listas não possuem numeros em comum')
else:
    print('Numeros presentes nas duas lista: ',l3)
