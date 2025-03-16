def busca_sequencial(array, target):
    for i in range(len(array)):  
        if array[i] == target:  
            return array[i], i  
    return -1, -1  

array = [10, 20, 30, 40, 50]  
target = 30  

resultado_valor, resultado_indice = busca_sequencial(array, target)

if resultado_valor != -1:
    print(f"Valor encontrado: {resultado_valor}")
    print(f"Valor encontrado no índice: {resultado_indice}")
else:
    print("Valor não encontrado.")




# BuscaSequencial(V, v)
#    n ← tamanho(V)
#    para i de 1 até n faça
#        se V[i] == v então
#            retorne i
#    retorne -1
