def subtract_raw(a: list[float], b: list[float], p=1.0) -> None:
    if len(a) != len(b):
        raise ValueError("wrong sizes")
    for i in range(len(a)):
        a[i] -= (p * b[i])

def divide_raw(a: list[float], p=1.0) -> None:
    for i in range(len(a)):
        a[i] /= p

def gauss(a: list[list[float]], b: list[float]) -> list[float]:
    if len(a) != len(b):
        raise ValueError("wrong sizes")

    n = len(a)
    for i in range(n):
        pivot = a[i][i]
        if pivot == 0:
            raise ValueError("Nie może być zero na diagonali")
        divide_raw(a[i], pivot)
        b[i] /= pivot

        for j in range(n):
            if j == i:
                continue
            factor = a[j][i]
            subtract_raw(a[j], a[i], factor)
            b[j] -= (b[i] * factor)

    return b