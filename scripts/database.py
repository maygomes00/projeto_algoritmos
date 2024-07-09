import sqlite3

#Função para criar database para o Grafo
def database():
    condb = sqlite3.connect('graph.db')
    cursor = condb.cursor()
    #Criar tabela para o Grafo
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS graph (
        origem INTEGER,
        destino INTEGER,
        peso REAL
    )
    ''')
    #Inicializar e carregar arestas do Grafo
    arestas = []
    with open('data/bio-human-gene1.edges', 'r') as f:
        for linha in f:
            partes = linha.split()
            origem = int(partes[0])
            destino = int(partes[1])
            peso = int(partes[2])
            arestas.append((origem, destino, peso))

    cursor.executemany('INSERT INTO graph (origem, destino, peso) VALUES (?, ?, ?)', arestas)
    condb.commit()
    #Fechar conexão do database
    condb.close()
