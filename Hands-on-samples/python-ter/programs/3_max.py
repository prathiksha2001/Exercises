ls1 = [2,1,4,5,6,4,3,6,8,9,7,0,100,5,50,50,25,25]
ls1 = list(set(ls1))

n = 0
while n < 2:
    ls1.remove(max(ls1))
    n += 1

print(max(ls1))