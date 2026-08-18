def ler_matriz(tamanho=10):
    return [[int(x) for x in input(f"Linha {i}: ").split()] for i in range(tamanho)]


def produto_escalar(a, b, tamanho=10):
    return sum(a[i][j] * b[i][j] for i in range(tamanho) for j in range(tamanho))


if __name__ == "__main__":
    print("Matriz A (10 valores por linha):")
    a = ler_matriz()

    print("Matriz B (10 valores por linha):")
    b = ler_matriz()

    print(f"Resultado: {produto_escalar(a, b)}")
