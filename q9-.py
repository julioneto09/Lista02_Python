'''
Crie duas listas com números de 0 a 9, embaralhe as listas e sorteie um número de cada
uma para formar uma dezena, repita a operação 5 vezes para sortear 5 dezenas, assim
como na mega sena. Caso a dezena caia como 00 (zero, zero) faça o sorteio dela
novamente até sair outra combinação. Depois disso exiba as dezenas sorteadas.
'''
import random

l1 = []
l2= []
d=[]
for k in range(0,10):
    l1.append(k)
    l2.append(k)

for c in range(5):
        random.shuffle(l1)
        random.shuffle(l2)
        d.append((l1[0],l2[0]))
                   
print ('Dezenas sorteadas: ', d)