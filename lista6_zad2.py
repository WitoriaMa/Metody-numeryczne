def parabol(f, a, b, n):
    if n% 2 == 1:
        raise ValueError("n musi być parzyste")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n-1, 2):
        s += 2 * f(a + i * h)
    return s * h / 3

n=100

print(parabol(lambda x: x**2, 0, 1, n)-1/3)
print(parabol(lambda x: x**3, 0, 1, n)-1/4)
print(parabol(lambda x: x**4, 0, 1, n)-1/5)
print(parabol(lambda x: x**5, 0, 1, n)-1/6)
print(parabol(lambda x: x**6, 0, 1, n)-1/7)
print(parabol(lambda x: x**7, 0, 1, n)-1/8)
