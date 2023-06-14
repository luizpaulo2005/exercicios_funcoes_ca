def calcularImposto (renda, rendaMinima, baseCalculo, baseAdicional):
  taxaBasica = min(renda, rendaMinima)
  taxaAdicional = max((renda-rendaMinima), 0)
  return taxaBasica + (taxaAdicional * baseAdicional)

meuImposto = calcularImposto(800, 150, 200, 100)
print(meuImposto)

# 1 - Qual é o valor impresso no console ao final da sua execução?
# 65150

# As linhas do programa estão numeradas de 1 a 8. Qual a sequência em que essas linhas são executadas?
# 6, 1, 2, 3, 4, 7

# Na linha 2, quanto valem os parâmetros renda, rendaMinima, baseCalculo e baseAdicional?
# 800, 150, 200, 100