
g = globals()
print(g)
x = 'foo'
print(g)
print('\n\n')
def f(x, y):
    s = 'foo'
    print(locals())
print('\n\n')
f(3.5,7)

def f():
    x = 20

    def g():
        nonlocal x
        x = 40
    g()
    print('%d' % (x))
f()


