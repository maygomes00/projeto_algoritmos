import tkinter as tk
import networkx as nx

def visu_graph(grafo, caminho):
    root = tk.Tk()
    root.title("Visualização do Grafo | Caminho mais Curto")

    canvas_width = 900
    canvas_height = 700
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
    canvas.pack()

    pos = nx.spring_layout(grafo)
    
    # Normalizar as coordenadas para o intervalo [0, 2]
    min_x = min(pos[node][0] for node in pos)
    min_y = min(pos[node][1] for node in pos)
    max_x = max(pos[node][0] for node in pos)
    max_y = max(pos[node][1] for node in pos)

    for node in pos:
        pos[node] = (
            2 * (pos[node][0] - min_x) / (max_x - min_x),
            2 * (pos[node][1] - min_y) / (max_y - min_y)
        )

    def draw_graph():
        canvas.delete("all")

        # Desenhar arestas
        for u, v, data in grafo.edges(data=True):
            x1, y1 = pos[u]
            x2, y2 = pos[v]
            canvas.create_line(x1 * canvas_width / 2, y1 * canvas_height / 2, x2 * canvas_width / 2, y2 * canvas_height / 2, fill="#727B8C")
        
        # Desenhar nós
        for n in grafo.nodes():
            x, y = pos[n]
            canvas.create_oval(x * canvas_width / 2 - 8.5, y * canvas_height / 2 - 8.5, x * canvas_width / 2 + 8.5, y * canvas_height / 2 + 8.5, fill="#060644", outline="#060644")
            canvas.create_text(x * canvas_width / 2, y * canvas_height / 2, text=str(n), fill="white", font=("Palatino", 10))

        # Desenhar caminho
        if caminho:
            for i in range(len(caminho) - 1):
                u = caminho[i]
                v = caminho[i + 1]
                x1, y1 = pos[u]
                x2, y2 = pos[v]
                canvas.create_line(x1 * canvas_width / 2, y1 * canvas_height / 2, x2 * canvas_width / 2, y2 * canvas_height / 2, fill="#FCC931", width=2)

    draw_graph()
    root.mainloop()
