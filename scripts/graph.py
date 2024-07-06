import sqlite3
import networkx as nx

#Função para inicializar Grafo do database
def initialize_graph():
    #Conectando com o database de graph
    condb = sqlite3.connect('graph.db')
    cursor = condb.cursor()
    cursor.execute('SELECT origem, destino, peso FROM graph')
    #Retorno da busca ao database
    arestas = cursor.fetchall()
    #Fechar conexão do database
    condb.close()
    #Criando um grafo
    Grafo = nx.DiGraph()
    for origem, destino, peso in arestas:
        #No grafo criado, adicionar aresta do database
        Grafo.add_edge(origem, destino, weight=peso)
    return Grafo

#Algoritmo Dijkstra
def dijkstra(grafo, origem, destino):
    #Incialzar distâncias dos nós aos nós de origem 
    distancias = {}
    for no in grafo.nos:
        distancias[no] = float('inf')
    distancias[origem] = 0
    #Inicializar nó anterior dos nós nos caminhos mais curtos
    caminho_ant = {}
    for no in grafo.nos:  
        caminho_ant[no] = None
    n_visitados = list(grafo.nos)

    while n_visitados:
        #Mapear nó não visitado com menor distância
        no_atual = min(n_visitados, key=lambda no: distancias[no])
        n_visitados.remove(no_atual)

        if distancias[no_atual] == float('inf'):
            break

        for vizinho, dados in grafo[no_atual].items():
            peso = dados['weight']
            distancia = distancias[no_atual] + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho_ant[vizinho] = no_atual

    # Reconstrói o caminho mais curto
    caminho_curto = []
    no_atual = destino
    while no_atual is not None:
        caminho_curto.append(no_atual)
        no_atual = caminho_ant[no_atual]
    caminho_curto = caminho_curto[::-1]

    return caminho_curto, distancias
