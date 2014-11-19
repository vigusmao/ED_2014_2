from random import randint

N = 400
MAX = 20000

def gerar_lista():
    lista = []
    for i in range(N):
        lista += [randint(1, MAX)]
    return lista



def encontrar_tuplas_n4(lista):
    cont = 0
    for x in range(0, N):
        for y in range(x+1, N):
            for z in range(y+1, N):
                for w in range(z+1, N):
                    if lista[x] + lista[y] == lista[z] + lista[w]:
                        # print("(%d, %d, %d, %d)" % (x, y, z, w))
                        cont += 1
    print(cont)



def encontrar_tuplas_n2(lista):
    cont = 0

    tabela = {}  # tabela hash {chave: valor} (dict)
    for x in range(0, N):
        for y in range(x+1, N):
            soma = lista[x] + lista[y]

            if soma in tabela:
                lista_de_pares = tabela[soma]
            else:
                lista_de_pares = []
                tabela[soma] = lista_de_pares

            lista_de_pares += [(x, y)]

    for soma in tabela:
        lista_de_pares = tabela[soma]
        tamanho = len(lista_de_pares)
        if tamanho > 1:
            cont += int(tamanho * (tamanho - 1) / 2)
            
    print(cont)


lista = gerar_lista()
# print("lista =", lista)
encontrar_tuplas_n2(lista)

    
