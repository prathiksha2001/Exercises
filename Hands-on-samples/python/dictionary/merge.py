dict1 = {'a': 97, 'b': 98}
dict2 = {'c': 99, 'd': 100}
#dict1.update(dict2)
print(dict1)
dict3 = {1: 'hi', 2: 'hello'}
#dict2.update(dict3)
print(dict2)
res = {**dict1, **dict3, **dict2}
result = dict1 | dict2 | dict3
print(res)
print(result)