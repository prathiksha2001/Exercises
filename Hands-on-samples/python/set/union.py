x1 = {'foo','bar','baz'}
x2 = {'baz','qux','quux'}
ls1 = [1,3,4,5,6,7,8]
print(x1 | x2)
x1 = x1.union(ls1)
print(x1)
if __name__ == '__main__':
    # print(x1 | x2)
    pass