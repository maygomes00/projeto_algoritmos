# Projeto de Algoritmos 2024.1: Grafo em Dijkstra

Este projeto foi criado para a disciplina de Algoritmos e Estrutura de Dados do cruso Sistemas de Informação no Centro de Informática UFPE em 2024.1
Criado por: Mayara Gomes de Oliveira Pina (mgop)

## Projeto
Calcula o melhor caminho entre dois pontos em um grafo utilizando o algoritmo de Dijkstra. O grafo é construído a partir de um banco de dados SQLite e o caminho mais curto é visualizado graficamente.

## Dependências

- Python 3.12
- sqlite3
- networkx
- matplotlib
- tkinter

## Uso

1. Rode o ambiente virtual ``venv`` (vá até o cd do projeto):
    ```
    $source venv/bin/activate
    ```
2. Execute o script principal `main.py`:
    ```
    $python main.py
    ```
3. Siga as instruções em tela para inserir os inputs: o nó de origem e o nó de destino.

## Estrutura do Projeto

- `data/`: Pasta contendo o arquivo de dados do grafo.
- `database.py`: Arquivo para criação e inicialização do Database.
- `graph.py`: Arquivo para carregar o grafo e implementar o algoritmo de Dijkstra.
- `main.py`: Aquivo principal do Projeto.
- `visualization.py`: Arquivo para visualização gráfica do grafo.
