from operator import itemgetter

fruits = {"apple":200, "orange": 180, "banana" : 60, "kiwi": 240}

print(sum(fruits.values()))
print(len(fruits))
print(str(fruits.__sizeof__()) + " bytes")

ls1 = [{"name": "Nandini", "age": 20},
       {"name": "yazhan", "age": 20},
       {"name": "Nikhil", "age": 19}]

print(sorted(ls1, key = lambda i: i['age']))
# print(sorted(ls1, key = itemgetter('age'))) 

# print("")
# print(sorted(ls1, key = itemgetter('name')))
# print("")
# print(sorted(ls1, key = itemgetter('age','name')))
# print("")
# print(sorted(ls1, key = itemgetter('age'), reverse=True))

