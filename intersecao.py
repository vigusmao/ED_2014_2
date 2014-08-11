from random import randint
from time import time

TAMANHO = 10**4

def calcula_intersecao(a, b):

    resultado = []

    for elemento in a:
        if (elemento in b) and (elemento not in resultado):
            resultado += [elemento]

    return resultado

def calcula_intersecao_bombado(a, b):
    resultado = set()

    conjunto_b = set()
    for elemento in b:
        conjunto_b.add(elemento)

    for elemento in a:
        if elemento in conjunto_b:
            resultado.add(elemento)

    return list(resultado)
            

def gera_lista(tamanho):
    lista = [] 
    for i in range(tamanho):
        lista += [randint(1, 10**5)]
    return lista
    

#main

print("Gerando listas...")
inicio = time()
lista1 = gera_lista(TAMANHO)
lista2 = gera_lista(TAMANHO)
tempo_total = time() - inicio
print("levou %.6f segundos" % tempo_total)

print("\nCalculando intersecao...")
inicio = time()
intersecao = calcula_intersecao(lista1, lista2)
tempo_total = time() - inicio
print("tamanho da intersecao = %d" % len(intersecao))
print("levou %.6f segundos" % tempo_total)

print("\nCalculando intersecao (bombado)...")
inicio = time()
intersecao = calcula_intersecao_bombado(lista1, lista2)
tempo_total = time() - inicio
print("tamanho da intersecao = %d" % len(intersecao))
print("levou %.6f segundos" % tempo_total)







