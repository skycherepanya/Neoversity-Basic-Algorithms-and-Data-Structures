import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Метро Будапешта
m1 = [("Vörösmarty tér", "Deák Ferenc tér", 2), ("Deák Ferenc tér", "Oktogon", 3), ("Oktogon", "Hősök tere", 4)]
m2 = [("Széll Kálmán tér", "Batthyány tér", 2), ("Batthyány tér", "Deák Ferenc tér", 3), ("Deák Ferenc tér", "Astoria", 2), ("Astoria", "Keleti pályaudvar", 3)]
m3 = [("Nyugati pályaudvar", "Deák Ferenc tér", 3), ("Deák Ferenc tér", "Kálvin tér", 2), ("Kálvin tér", "Corvin-negyed", 2)]
m4 = [("Szent Gellért tér", "Kálvin tér", 3), ("Kálvin tér", "Keleti pályaudvar", 4), ("Keleti pályaudvar", "II. János Pál pápa tér", 2)]


def add_edges(graph, lines):
    for u, v, w in lines:
        graph.add_edge(u, v, weight=w)

add_edges(G, m1)
add_edges(G, m2)
add_edges(G, m3)
add_edges(G, m4)


if __name__ == "__main__":
    print(f"Вершин: {G.number_of_nodes()}")
    print(f"Ребер: {G.number_of_edges()}")

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))

    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightgray')
    nx.draw_networkx_labels(G, pos, font_size=10)

    nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for u,v,w in m1], edge_color='gold', width=3, label="M1")
    nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for u,v,w in m2], edge_color='red', width=3, label="M2")
    nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for u,v,w in m3], edge_color='blue', width=3, label="M3")
    nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for u,v,w in m4], edge_color='green', width=3, label="M4")

    plt.legend()
    plt.axis('off')
    plt.show()