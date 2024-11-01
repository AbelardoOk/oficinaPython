import random

colunas = 5
linhas = 4
matriz = [[],[]]

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = random.randint(0,10)


print(matriz)