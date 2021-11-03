'''
Faça um programa que exiba uma lista formada pelos X primeiros números primos de
uma dada lista. A lista dos números primos deverá ser originada, através de uma lista
formada por números inteiros de 1 até 200. A ideia é deixar que o usuário defina o
número X (quantidade de números primos).
'''
l=[]
for k in range(1,200):
    l.append(k)

x = int(input('Informe a quantidade de numeros primos buscada: '))

q=0
p=[]
erro = 0

'''o if da a condição de funcionamento do for
o segundo for começa em 2 porque todos os números são divisiveis por 1'''
for w in range(0, 200):
    if x > q :
        for z in range(2, w):
            if (l[w] % z) == 0:
                break
        else:
            p.append(l[w])
            q = q + 1
            
print(f'\nPrimeiros {x} números primos: {p}')

        