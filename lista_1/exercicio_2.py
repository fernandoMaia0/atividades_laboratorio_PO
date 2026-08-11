# Lê o mesmo grafo do exercício 1 e calcula o grau de cada vértice
# (quantidade de arestas incidentes, considerando apenas se ha ou nao aresta).

from exercicio_1 import ler_grafo


def calcular_graus(matriz):
    n = len(matriz)
    graus = []
    for i in range(n):
        grau = sum(1 for j in range(n) if matriz[i][j] > 0)
        graus.append(grau)
    return graus


if __name__ == "__main__":
    matriz_adjacencia = ler_grafo("grafo.txt")
    graus = calcular_graus(matriz_adjacencia)

    print("Grau de cada vértice:")
    for vertice, grau in enumerate(graus):
        print(f"Vértice {vertice}: grau {grau}")
