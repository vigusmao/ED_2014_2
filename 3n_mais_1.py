from time import time

TAMANHO_MEMO = 1000000
## Coloque TAMANHO_MEMO = 0 na linha acima para "desligar" a memoizacao

memo = [0] * TAMANHO_MEMO
## Optamos por criar uma tabela (array) para memoizacao com visibilidade
## global, de forma a nao termos que passa-la como parametro entre as
## chamadas recursivas. Este eh um dos (poucos) casos em que variaveis
## globais sao aceitas, e ate mesmo recomendaveis.


def f(n):
    if n % 2 == 0:
        return n//2
    return 3*n + 1


def tamanho(n):
    if n < TAMANHO_MEMO:
        memo_result = memo[n]
        if memo_result != 0:
            return memo_result

    result = 0
    if n == 1:
        result = 1
    else:
        result = 1 + tamanho(f(n))

    if n < TAMANHO_MEMO:
        memo[n] = result

    return result

    
    
## MAIN
    
while True:

    a = eval(input("\nmin_n = "))
    b = eval(input("max_n = "))
    
    maior = None
    tamanho_maior = 0

    start = time()
    
    for i in range(a, b+1):
        t = tamanho(i)
        if t > tamanho_maior:
            tamanho_maior = t
            maior = i

    print("tempo total = %.8f" % (time() - start))

    print("O numero do intervalo que tem a maior sequencia eh %d" % maior)
    print("tamanho(%d) = %d" % (maior, tamanho_maior))
