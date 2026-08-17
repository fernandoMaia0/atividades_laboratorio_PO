from exercicio_1 import Grafo


def custo_itinerario(grafo, itinerario):
    return sum(
        grafo.adj[itinerario[i]][itinerario[i + 1]]
        for i in range(len(itinerario) - 1)
    )


if __name__ == "__main__":
    g = Grafo.carregar_de_arquivo("grafo.txt")

    n = int(input("Quantos itinerários? "))
    for i in range(n):
        cidades = input(f"Itinerário {i} (cidades separadas por espaço): ")
        itinerario = [int(c) for c in cidades.split()]
        print(f"Custo do itinerário {i}: {custo_itinerario(g, itinerario)}")
