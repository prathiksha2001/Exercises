sample = ['Gfg', 3, 'is', 8, 'Best', 10, 'for', 18, 'Geeks', 33]
key_list = ["name", "number"]
res = []
for i in range(0,len(sample),2):
    res.append({key_list[0]:sample[i], key_list[1]:sample[i+1]})

print(res)