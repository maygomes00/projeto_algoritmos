from scripts.database import database
from scripts.graph import dijkstra, initialize_graph
from scripts.visualization import visu_graph

if __name__ == "__main__":
    #Carregar dados do database
    database()
    #Inicializar grafo
    Grafo = initialize_graph()

    origem = int(input("Digite o nó de origem: "))
    destino = int(input("Digite o nó de destino: "))
    #Chamar a função Dijkstra para calcular o caminho mais curto e as distâncias do nó de origem ao nó de destino
    caminho, distancias = dijkstra(Grafo, origem, destino)

    #Caminho infinito == inexistente
    if distancias[destino] == float('inf'):
        print(f"Não há caminho disponível de {origem} para {destino}.")
    else:
        # Exibe o caminho mais curto
        print(f"O caminho mais curto de {origem} para {destino} é: {caminho}")
        
        # Exibe a distância total do caminho mais curto
        print(f"A distância total é: {distancias[destino]}")

    visu_graph(Grafo, caminho)