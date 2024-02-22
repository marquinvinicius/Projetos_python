from random import randint
from pandas import DataFrame as dt
from base import *
dados = []
v = randint(5, 20)
for p in range(1, v):
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    n3 = randint(1, 10)
    n4 = randint(1, 10)
    me = (n1 + n2 + n3 + n4) / 4
    if me >= 7:
        res = 'Aprovado'
    else:
        res = 'Reprovado'
    dados.append([nomes(), n1, n2, n3, n4, me, res])

for x in range(0, len(dados)):
    for z in range(x + 1, len(dados)):
        if dados[x][0] > dados[z][0]:
            y = dados[x][0]
            dados[x][0] = dados[z][0]
            dados[z][0] = y
            
# Uso o pandas para deixar os dados mais apresentaveis
b = dt(dados, index=range(1, v), columns=['Aluno', 'Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Media', 'Status'])


print(b)
