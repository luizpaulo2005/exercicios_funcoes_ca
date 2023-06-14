import math


def calculaDistancia(x, y):
    return math.dist(x, y)


caso1 = calculaDistancia([1, 2], [2, 3])
print(caso1)
caso2 = calculaDistancia([2, 6], [7, 2])
print(caso2)
caso3 = calculaDistancia([3, 4], [5, 6])
print(caso3)
caso4 = calculaDistancia([7, 2], [4, 6])
print(caso4)
caso5 = calculaDistancia([10, 9], [23, 1])
print(caso5)