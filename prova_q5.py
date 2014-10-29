memo = [None] * 10001


def calcula(y):
    # leio do memo
    if memo[y] is not None:
        return memo[y]

    
    if y <= 5:
        resultado = y
    elif y % 2 == 0:
        resultado = calcula(y//2) + calcula(y-1)
    else:
        resultado = calcula(y-3) - calcula(y-2) + calcula(y-1)


    # escrevo no memo
    memo[y] = resultado

    return resultado





