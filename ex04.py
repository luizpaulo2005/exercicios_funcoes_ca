import math

def calculaDiferenca(x, y):
    if x > y:
        return x - y
    else:
        return y - x

def calculaQuadrado(x):
    return x * x

def calculaDistancia(x, y):
    return math.dist(x, y)


caso0_1 = calculaDiferenca(2, 1)
print(caso0_1)
caso0_2 = calculaDiferenca(5, 3)
print(caso0_2)
caso0_3 = calculaDiferenca(10, 5)
print(caso0_3)

caso1_1 = calculaDistancia([1, 2], [2, 3])
print(caso1_1)
caso1_2 = calculaDistancia([2, 6], [7, 2])
print(caso1_2)
caso1_3 = calculaDistancia([3, 4], [5, 6])
print(caso1_3)

caso2_1 = calculaQuadrado(2)
print(caso2_1)
caso2_2 = calculaQuadrado(9)
print(caso2_2)
caso2_3 = calculaQuadrado(10)
print(caso2_3)