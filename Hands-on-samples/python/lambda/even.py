#split even numbers using lambda function

list1 = [1,2,3,4,5,6,7,8,9,10]

#even = lambda x : print(f"{x} is even") if (x % 2 == 0) else print(f"{x} is odd")
even = lambda x : x % 2 == 0
output = list(filter(even,list1))

print(output)
#square of elements in list
sq = list(map(lambda x: x**2, list1))
print(sq)

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x if x%2==0 else None, li))
print(list(evenNumbers))