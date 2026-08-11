# Lê um arquivo com a descrição de um grafo (não-direcionado, com pesos)
# e monta a matriz de adjacência correspondente.


def ler_grafo(caminho):
    with open(caminho, "r") as f:
        n = int(f.readline().strip())
        matriz = [[0] * n for _ in range(n)]

        for linha in f:
            if not linha.strip():
                continue
            origem, destino, peso = map(int, linha.split())
            matriz[origem][destino] = peso
            matriz[destino][origem] = peso

    return matriz


def exibir_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(v) for v in linha))


if __name__ == "__main__":
    matriz_adjacencia = ler_grafo("grafo.txt")
    print("Matriz de Adjacência:")
    exibir_matriz(matriz_adjacencia)
