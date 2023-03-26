tup1 = (1,2,3,4,5,6,7,8,9,10)
list1 = []
for i in tup1:
    if i % 2 == 0:
        list1.append(i)

print(tuple(list1))

even = lambda x : x if (x % 2 ==0) else None
res = list(filter(even,tup1))

print(res)