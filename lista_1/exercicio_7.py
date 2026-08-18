def termo(i):
    return (2 * i - 1) / ((-2) ** (i + 1))


def somatorio(n):
    return sum(termo(i) for i in range(1, n + 1))


if __name__ == "__main__":
    n = int(input("Digite o valor de n: "))
    print(f"S = {somatorio(n)}")
