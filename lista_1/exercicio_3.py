from exercicio_1 import Grafo


def vertices_adjacentes(grafo, vertice):
    return [v for v, peso in enumerate(grafo.adj[vertice]) if peso != 0]


if __name__ == "__main__":
    g = Grafo.carregar_de_arquivo("grafo.txt")

    vertice = int(input(f"Digite um vértice (0 a {g.n - 1}): "))
    print(f"Vértices adjacentes a {vertice}: {vertices_adjacentes(g, vertice)}")
