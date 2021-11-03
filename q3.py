'''
Escreva um programa que solicite ao usuário 10 valores (1 até 10) e guarde-os em uma
tupla. O programa deverá realizar uma análise dos valores inseridos e exibir:
a. Quantas vezes o número 5 foi digitado;
b. Qual a posição do número 3;
c. Quantos números pares e ímpares foram digitados, informe quais foram.
'''


numero = 10
q = [1,2,3,4,5,6,7,8,9,10]
r=[]
for k in range(10):
    while True:
        try:
            q[k] = int(input('Informe um número para a sequência: '.format(k)))
            if (q[k] >= 0) and (q[k] <= 10):
                break
            else:
                print('Escreva um número inteiro entre 0 e 10!')
        except: 
            ValueError
            print('Escreva um número inteiro entre 0 e 10!')
    r.append(q[k])

count = r.count(5)

par = 0
impar = 0
p=[]
i=[]

for l in range(10):
    if (r[l]%2)==0:
        par += 1
        p.append(r[l])       
    else:
        impar += 1
        i.append(r[l])

print(f'\na) O numero 5 foi digitado {count} vezes')
print(f'\nb) O numero 3 esta na poisção {r.index(3)} da lista')
print(f'\nc) temos {par} numeros pares: {p} e {impar} numeros ímpares: {i}')
