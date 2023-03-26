test_list = ["Gfg", "is", "Best"]
subs_dict = {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}
k = 1

for i, item in enumerate(test_list):
    if subs_dict.get(item) != None:
        test_list[i] = subs_dict[item][k]

print(test_list)
