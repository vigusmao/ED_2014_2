from time import time
from random import randint
import heapq 

N = 10**6
K = 400


def cria_lista():
    lista = []
    for i in range(N):
        lista += [randint(1, 10**7)]
    return lista


def top_k_ordenando(lista, k):
    lista_ordenada = sorted(lista, reverse=True)
    top_k = lista_ordenada[:k]
    return top_k

def top_k_usando_heap(lista, k):
    top_k = heapq.nlargest(k, lista)
    return top_k

def top_k_usando_array(lista, k):
    array = sorted(lista[:k])
    for elemento in lista[k:]:
        if elemento > array[0]:
            array[0] = elemento
            i = 0
            while array[i+1] < array[i]:
                array[i+1], array[i] = array[i], array[i+1]
                i += 1
                if i == k-1:
                    break
    return array[-1::-1]


print("N = %d" % N)
print("K = %d" % K)

start = time()
minha_lista = cria_lista()
print("tempo para gerar a lista = %.5f" % (time() - start))


start = time()
maiores = top_k_ordenando(minha_lista, K)
print("tempo para obter o top k usando ordenacao = %.5f" % (time() - start))
#print(maiores)

start = time()
maiores = top_k_usando_array(minha_lista, K)
print("tempo para obter o top k usando array = %.5f" % (time() - start))
#print(maiores)

start = time()
maiores = top_k_usando_heap(minha_lista, K)
print("tempo para obter o top k usando heap = %.5f" % (time() - start))
#print(maiores)


