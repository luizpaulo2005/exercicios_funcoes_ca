def calcularMedia(num1, num2, num3):
    media = (num1 + num2 + num3) / 3
    aprovado = media >= 6


    if (aprovado):
        return "Aprovado"
    else:
        return "Reprovado"

resultadoAluno1 = calcularMedia(3, 6, 9)
print(resultadoAluno1)
resultadoAluno2 = calcularMedia(4, 3, 5)
print(resultadoAluno2)
resultadoAluno3 = calcularMedia(8, 9, 10)
print(resultadoAluno3)
resultadoAluno4 = calcularMedia(7, 6, 5)
print(resultadoAluno4)
resultadoAluno5 = calcularMedia(9, 3, 2)
print(resultadoAluno5)