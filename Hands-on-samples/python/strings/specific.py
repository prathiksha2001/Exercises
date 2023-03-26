test_list = ["geeksforgeeks is best for geeks"]
char_list = ["e","b","g","f"]

dict1 = {}

for i in range(len(char_list)):
    dict1[char_list[i]] = str(test_list).count(char_list[i])

print(dict1)
