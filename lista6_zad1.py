def trapez(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return s * h

 
if __name__ == "__main__":
    print(trapez(lambda x: x**2, 0, 1, 10)-1/3)
    print(trapez(lambda x: x**3, 0, 1, 10)-1/4)
    print(trapez(lambda x: x**4, 0, 1, 10)-1/5)
    print(trapez(lambda x: x**5, 0, 1, 10)-1/6)

#im większe n tym mniejszy bład
