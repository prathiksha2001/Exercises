x1 = {'foo','bar','baz'}
x2 = {'baz','qux','quux'}
x3 = {'bar','qux','quux'}
x4 = {'bar','qux','quux'}
x5 = {'bar','qux','quux','oo'}
# x1 |= x2
print(x1 & x2)
print(x1.intersection(x2))
print("\ndifference")
print(x1-x2)
print(x1.difference(x2,x3,x4))
print("\nsymmetric_difference")
print( x1.symmetric_difference(x2))
print(x1^x2)
print('\n')
print("Common elements from x1 and x2")
print(x1.isdisjoint(x4))
print(x1.intersection(x4))
print("\nfinding subset: ")
print(x3.issubset(x4) and x3 <= x4)
print(x3.issubset(x5) and x3 != x5)
print(x3 < x5)
print("\n superset")
print(x5.issuperset(x3))
print(x4 >= x3)
print("\n superset")
print(x3.issuperset(x4))
print(x4.issuperset(x3))
print(x5 > x3)

x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}
# print("\n update")
# x1 |= x2
# x1.update(x2)
# print(x1)
# print("\n insertion update: ")
# x1 &= x2
# x1.intersection_update(x2)
# print(x1)
# print("\n difference update: ")
# x1 -= x2
# x1.difference_update(x2)
# print(x1)
print("\n symmetric difference update: ")
# x1 ^= x2
# x1.symmetric_difference_update(x2)
# print(x1)

x1.add(2)
print(x1)
x1.remove(2)
print(x1)
x1.discard('foo')
print(x1.pop())
print(x1)
print(x1.clear())