#as 2 primeiras linhas pegam a entrada
#a 3 cria uma lista onde será salva os pedaços possiveis por cada corte

n = int(input())  #nao foi util no algoritmo, mas fazia parte da questao
alt_papel = list(map(int, input().split()))
total_pedaco = []

#esse for percorre todas as alturas uteis para um bom corte
for alt_corte in range(min(alt_papel), max(alt_papel)):

    #cortes com mesma altura dos pedaços nao é o ideial para ter mais pedaços, portanto, pode ser descartado
    if alt_corte not in alt_papel:
        lado = 'baixo'
        pedaco = 1

        #a ideia a considerar é contar a peca de baixo como uma só, e sempre que algum pedaço ultrapassar
        #a altura do corte da qual está sendo considerada, ele seja contada como um pedaço a ser cortado
        for alt_pedacos in alt_papel:
            if alt_pedacos > alt_corte and lado == 'baixo':
                pedaco += 1
                lado = 'cima'
            elif alt_pedacos < alt_corte:
                lado = 'baixo'

        #essa quantidade de cortes é salva numa lista com todas as quantidades de pedaços possiveis
        total_pedaco.append(pedaco)

#pra finalizar, é só printar o numero maximo de pedaços dessa lista
print(max(total_pedaco))
