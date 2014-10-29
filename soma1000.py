from random import randint

N = 10**4


def criar_lista():
    resultado = set()
    while len(resultado) < N:
        elemento = randint(-10**5, 10**5)
        resultado.add(elemento)
    return list(resultado)

def procurar_pares_1(lista):
    cont = 0
    for i in range(N):
        elemento1 = lista[i]
        for j in range(i+1, N):
            elemento2 = lista[j]
            if elemento1 + elemento2 == 1000:
                cont += 1
    return cont

def procurar_pares_2(lista):
    cont = 0
    tabela = set()

    # inserir na tabela hash
    for i in range(N):
        elemento = lista[i]
        tabela.add(elemento)   # tempo medio O(1)

    # buscar os complementos
    for i in range(N):
        elemento = lista[i]
        complemento = 1000 - elemento
        if complemento in tabela:   # tempo medio O(1)
            cont += 1
        
    return cont/2    


# main

print("gerando lista")
lista = criar_lista()
print("procurando pares (sem hashing)")
print("cont_pares (1) = %d" % procurar_pares_1(lista))
print("procurando pares (com hashing)")
print("cont_pares (2) = %d" % procurar_pares_2(lista))



