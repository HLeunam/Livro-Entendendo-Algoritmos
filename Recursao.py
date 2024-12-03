# Método sem utilizar recursão.
def procura_pela_chave(caixa_principal):
    pilha = main_box.crie_planilha_busca()

    while pilha is not vazia:
        caixa = pilha.pegue_caixa()
        for item in caixa:
            if item.e_uma_caixa():
                pilha.append(item)
            elif item.e_uma_chave():
                print("Achei a chave!")

# Maneira utilizando a recursão.
def procure_pela_chave(caixa):
    for item in caixa:
        if item.e_uma_caixa():
            procure_pela_chave(item)
        elif item.e_uma_chaave():
            print("Achei a chave!")