ls1 = [5,4,3,1,6,7,2,9,8]

key = 1
no_of_moves = 1
while no_of_moves != 0:
    no_of_moves = 0
    for i in range(1,len(ls1)):
        if(ls1[i-1]>ls1[i]):
            ls1[i],ls1[i-1] = ls1[i-1],ls1[i]
            no_of_moves += 1
print(ls1) 
