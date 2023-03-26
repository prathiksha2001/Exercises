test_dict = {'Manjeet': [1, 4, 5, 6],
             'Akash': [1, 8, 9],
             'Nikhil': [10, 22, 4],
             'Akshat': [5, 11, 22]}

x = []
for i in test_dict.keys():
    x.extend(test_dict[i])

print(x)

unique = []
for i in range(len(x)):
    if(x.count(i)==1):
        unique.append(i)

print(unique)

for i in test_dict.keys():    
    a = []
    for j in test_dict[i]:
        if j in unique:
            a.append(j)
    test_dict[i] = a

print(test_dict)
            

print(test_dict)

