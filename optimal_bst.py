def get_custo(i, j, pd_custo):
    n = len(pd_custo)

    # para posicoes que caem fora da tabela, retorne 0
    # (correspondem a conjuntos vazios de chaves)
    if j < i:
        return 0
    if i >= n or j >= n or i < 0 or j < 0:
        return 0
    
    return pd_custo[i][j]
    

def optimal_bst(freq):

    n = len(freq)
    pd_custo = []
    pd_raiz = []
    for i in range(n):
        pd_custo += [[0]*n]
        pd_raiz += [[-1]*n]

    for dif in range(n):
    # dif vai de 0 a n-1 (primeiro faz a diagonal principal, etc.)

        for i in range(n-dif):  # i vai de 0 a n-dif-1
            j = i + dif

            soma_freq = sum(freq[i:j+1])  # soma das freqs de i a j

            custo_minimo = -1
            raiz_minimo = None
            for r in range(i, j+1):  # r vai de i a j
                custo = get_custo(i, r-1, pd_custo) + \
                        get_custo(r+1, j, pd_custo) + \
                        soma_freq
                if custo < custo_minimo or (custo_minimo == -1):
                    custo_minimo = custo
                    raiz_minimo = r

            pd_custo[i][j] = custo_minimo
            pd_raiz[i][j] = raiz_minimo

    return pd_custo[0][n-1], pd_custo, pd_raiz




# main

freq = [8, 10, 2, 3, 6]
n = len(freq)
custo, m_custo, m_raiz = optimal_bst(freq)

print("custo minimo = %d" % custo)

print("\ncustos:")
for linha in m_custo:
    print(linha)

print("\nraizes")
for linha in m_raiz:
    print(linha)



# encontra a arvore otima baseado nas raizes de cada subproblema
pais = [-1]*n
fila = [(0,n-1,-1)]
indice_comeco = 0
while indice_comeco < len(fila):
    registro = fila[indice_comeco]
    indice_comeco += 1
    i = registro[0]
    j = registro[1]
    pai = registro[2]
    raiz = m_raiz[i][j]
    if i < raiz:
        fila += [(i, raiz-1, raiz)]
    if raiz < j:
        fila += [(raiz+1, j, raiz)]
    pais[raiz] = pai
        

for i in range(n):
    print("pai(%d) = %d" % (i, pais[i]))

