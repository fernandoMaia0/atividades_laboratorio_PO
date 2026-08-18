def soma_serie(n):
    return sum(i * (i + 1) for i in range(1, n + 1))


if __name__ == "__main__":
    n = int(input("Digite o valor de n: "))
    print(f"Soma: {soma_serie(n)}")
