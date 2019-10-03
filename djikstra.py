ver, ci, cf = map(int, input().split(' '))                  #bloco 1, esse bloco recebe a entrada do usuario
ci, cf = ci-1, cf-1                                         #a primeira entrada deve conter 3 digitos TODOS INTEIROS:
grafo = [[]for i in range(ver)]                             #EX para grafo de 6 vertices: 6 1 3
while 1:                                                    #o primeiro digito sao os vertices, o segundo o ponto de
    try:                                                    #de partida, o terceiro o de chegada. As proximas linhas
        a, b, p = map(int, input().split(' '))              #devem conter INFORMAÇOES DAS ARESTAS: ponto de saida dela,
        grafo[a-1].append((b-1, p))                         #ponto de chegada e seu peso, EX: 1 3 12
        grafo[b-1].append((a-1, p))                         #Nao é preciso informar a mesma aresta  de forma invertida,
    except ValueError:                                      #ao digitar 1 3 12 ele salva do ponto 1 ao 3 peso 12 e do
        break                                               #ponto 3 ao ponto 1 peso 12 tambem. as entradas param ao
                                                            #digitar uma LINHA VAZIA.
pesos = [[999999999] for i in range(ver)]                   #bloco 2, aqui sao criadas e preparadas listas que ajudaram
pesos[ci][0] = 0                                            #o algoritmo, sao todas as ferramentas extras necessarias
menor_caminho = [[999999999] for j in range(ver)]           #para o começo e meio do algoritmo.
fechados = []
visitar = []

fechados.append(ci)                                         #bloco 3, aqui ja começa o algoritmo, nesse bloco sao
for cidades in grafo[ci]:                                   #adicionados os pesos minimo das arestas ligadas ao ponto
    pesos[cidades[0]][0] = cidades[1]                       #inicial e preparada a primeira lista de visita
    visitar.append(cidades[0])
    menor_caminho[cidades[0]][0] = ci

while len(fechados) != ver:                                          #bloco 4, aqui se desenvolve o corpo do algoritmo.
    procurar = sorted(list(visitar), key=lambda a : pesos[a][0])     #Verifica peso da aresta, se for menor salva, se
    prox = 0                                                         #nao, segue caminho. ele segue uma ordem de ir pelo
                                                                     #caminho anterior de menor peso, sempre pelo menor.
    for i in procurar:                                               #o caminho fica salvo em outra lista contendo
        if i not in fechados:                                        #sempre o anterior daquele caminho.
            prox = i
            break

    for cidade in grafo[prox]:
        if cidade[0] == ci:
            continue
        novo_peso = pesos[prox][0] + cidade[1]
        if novo_peso <= pesos[cidade[0]][0]:
            pesos[cidade[0]][0] = novo_peso
            menor_caminho[cidade[0]][0] = prox
        if cidade[0] not in fechados and cidade[0] not in visitar:
            visitar.append(cidade[0])
    visitar.remove(prox)
    fechados.append(prox)

caminho = [cf+1]                                              #bloco 5, depois do bloco 4, o grafo está ajustado baseado
andar = cf                                                    #no ponto de partida. o ultimo bloco acessa o caminho na
while andar != 999999999:                                     #lista menor_caminho e transorma a informaçao salva ali
    caminho.append(menor_caminho[andar][0]+1)                 #na lista caminho, faz uns ajustes finais e mostra para o
    andar = menor_caminho[andar][0]                           #usuario o caminho percorrido e a distancia total
caminho.reverse()
caminho = caminho[1:]
print('o menor caminho é o da seguinte lista:', caminho)
print('e o seu custo é:', pesos[cf])