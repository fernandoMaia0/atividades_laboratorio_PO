class Grafo:
    """Representa um grafo não-direcionado e ponderado via matriz de adjacência."""

    def __init__(self, num_vertices):
        self.n = num_vertices
        self.adj = [[0] * num_vertices for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v, peso):
        self.adj[u][v] = peso
        self.adj[v][u] = peso

    def imprimir(self):
        largura = max(len(str(max(l))) for l in self.adj) + 1
        for linha in self.adj:
            print("".join(str(v).rjust(largura) for v in linha))

    @classmethod
    def carregar_de_arquivo(cls, caminho):
        with open(caminho) as arquivo:
            linhas = [l.split() for l in arquivo if l.strip()]

        n = int(linhas[0][0])
        grafo = cls(n)

        for u, v, peso in linhas[1:]:
            grafo.adicionar_aresta(int(u), int(v), int(peso))

        return grafo


if __name__ == "__main__":
    g = Grafo.carregar_de_arquivo("grafo.txt")
    print("Matriz de Adjacência:")
    g.imprimir()
