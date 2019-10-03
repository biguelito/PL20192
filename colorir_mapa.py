#a primeira linha de entrada é pra ser inserida todos os pontos do grafo
#as linhas seguintes sao as conexoes de cada vertice na ordem que foram informados na primeira linha

#esse bloco cria o grafo inserido pelo usuario

grafo = {}
mapa = input('diga os vertices [a b c e]: ').split(' ')
for termo in mapa:
    print('conexoes de', termo, '[b c]')
    grafo[termo] = input('>>>').split(' ')

#grafo criado
#essa linha cria uma lista com as chaves ordenadas pelo tamanho das listas dos seus itens

chaves_ordenadas = sorted(list(grafo.keys()), key=lambda a: len(grafo[a]), reverse=True)

#aqui começa o algoritmo, criando um contador para a cor, um dicionario para salvar a cor do vertice quando pintado
#e uma copia da lista mapa para poder alterar a original e reverter as mudanças

cor = 0
pintado = {}
for vertice in chaves_ordenadas:
    temp = mapa[:]
    cor = 0
    if vertice in pintado:
        continue

#ele pinta um vertice que nao esteja pintado e verifica os vertices proximos

    else:
        pintado[vertice] = cor

        for proximo in grafo[vertice]:
            if proximo in pintado and pintado[vertice] == pintado[proximo]:
                pintado[vertice] += 1

#apos pintar e verificar ele cria uma lista com os vertices sem ligaçao

        for tirar in grafo[vertice]:
            temp.remove(tirar)

#depois ele pinta esses vertices e veifica se há alguem proximo pintado igual

        for distantes in temp:
            pintado[distantes] = cor
            for proxdis in grafo[distantes]:
                if proxdis in pintado and pintado[proxdis] == pintado[distantes]:
                    pintado[distantes] += 1

print('o numero minimo de cores é', max(pintado.values())+1)