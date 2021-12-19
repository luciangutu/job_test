def gen(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


x = 5
g = gen(x)
while True:
    try:
        print(next(g))
    except StopIteration:
        break
