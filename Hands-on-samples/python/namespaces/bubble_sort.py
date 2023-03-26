ls1 = [5,4,8,3,6,9,1]
change = True
while change:
    change = False
    for i in range(len(ls1)-1):
        if(ls1[i]>ls1[i+1]):
            change = True
            ls1[i],ls1[i+1] = ls1[i+1], ls1[i]

print(ls1)