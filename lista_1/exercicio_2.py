from exercicio_1 import Grafo


def grau_do_vertice(grafo, vertice):
    return sum(1 for peso in grafo.adj[vertice] if peso != 0)


if __name__ == "__main__":
    g = Grafo.carregar_de_arquivo("grafo.txt")

    print("Grau de cada vértice:")
    for v in range(g.n):
        print(f"Vértice {v}: grau {grau_do_vertice(g, v)}")
