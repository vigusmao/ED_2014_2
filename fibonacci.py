def fib_nao_recursivo(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    indice = 2
    while indice < n:
        a, b = b, a+b
        indice += 1
    return b


def fib_recursivo(n):
    if n <= 2:
        return 1
    return fib_recursivo(n-1) + fib_recursivo(n-2)


def fib_memoization(n, memo=None):
    if memo is None:
        memo = [0]*(n+1)
    ## OBS.: optamos por criar a tabela (array) para memoizacao
    ##       localmente (na primeira chamada), passando-a como
    ##       parametro entre as chamadas recursivas


    memo_result = memo[n]
    if memo_result != 0:
        return memo_result

    result = 0
    if n <= 2:
        result = 1
    else:
        result = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)

    memo[n] = result
    return result



## MAIN

print("\nNao recursivo")
for i in range(1, 50):
    print ("fib(%d) = %d" % (i, fib_nao_recursivo(i)))

print("\nRecursivo COM memoizacao")
for i in range(1, 50):
    print ("fib(%d) = %d" % (i, fib_memoization(i)))

print("\nRecursivo SEM memoizacao")
for i in range(1, 50):
    print ("fib(%d) = %d" % (i, fib_recursivo(i)))
