def feb(n):
    a = 0
    b = 1
    for i in range(1,10):
        yield a
        c = a+b
        a = b
        b = c

result = feb(5)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))