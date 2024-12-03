# Pesquisa Binária.
def pesquisa_binaria(lista, item):
    baixo = 0 
    alto = len(lista) - 1 

    while baixo < alto:
        meio = (alto + baixo) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
        return None