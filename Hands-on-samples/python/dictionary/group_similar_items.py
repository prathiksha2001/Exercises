test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8] 
res = {}

for num in test_list:
    if res.get(num) != [num]:       
        res[num] = [num,num]
    # res[num].append(num)

print(res)