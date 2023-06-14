def anosFumando(idadeI, idadeF):
    return abs(idadeF - idadeI)

def cigarrosPorAno(ano, cigPorDia):
    return (anos * 365) * cigPorDia

def macosCigarro(cigsPorAno):
    return cigsPorAno / 20

def valorFumo(macos, valorMaco):
    return macos * valorMaco

anos = anosFumando(19, 65)
cpa = cigarrosPorAno(anos, 12)
ma = macosCigarro(cpa)
valorTotal = valorFumo(ma, 8.25)
print(f"O valor gasto foi de R${valorTotal:.2f}")