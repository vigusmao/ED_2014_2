from random import randint
from time import time



def caracter_mais_frequente(texto):
    """Retorna o caracter que aparece com maior frequencia no texto
       informado, e o numero de vezes que ele aparece.

       Note que a complexidade desse algoritmo eh quadratica no tamanho do texto,
       pois para cada caracter, o texto inteiro precisa ser percorrido.
    """

    maxcont = 0
    maxcaracter = None
    for caracter in texto:
        cont = 0
        for i in range(len(texto)):
            if texto[i] == caracter:
                cont += 1
        if cont > maxcont:
            maxcont = cont
            maxcaracter = caracter

    return maxcaracter, maxcont
            

def caracter_mais_frequente_usando_dicionarios(texto):
    """Retorna o caracter que aparece com maior frequencia no texto
       informado, e o numero de vezes que ele aparece.

       Note que o texto eh percorrido apenas uma vez.
       A cada caracter lido, um contador eh localizado no dicionario (hash map)
       em tempo constante e eh entao incrementado (ou inserido com valor 1,
       caso seja a primeira vez que aquele caracter eh encontrado).
    """

    contadores = {}
    for caracter in texto:
        cont = contadores.get(caracter, 0)
        cont += 1
        contadores[caracter] = cont

    maxcont = 0
    maxcaracter = None
    for caracter in contadores:
        if contadores[caracter] > maxcont:
            maxcont =  contadores[caracter]
            maxcaracter = caracter

    return maxcaracter, maxcont
            


# main

texto = []
for _ in range(5000):
    texto += [randint(1, 100)]


inicio = time()
caracter_mais_frequente(texto)
print("%.5f segundos" % (time() - inicio))


inicio = time()
caracter_mais_frequente_usando_dicionarios(texto)
print("%.5f segundos" % (time() - inicio))






    
