input =  details={'Name' : "Alice",
         'Age' : 21,
         'Degree' : "Bachelor Cse",
         'University' : "Northeastern Univ"}

with open('files/temp.txt','w') as fp:
    for key, value in input.items():
        fp.write('%s : %s\n' % (key,value))

result = {}
for i in range(10):
    result[i+1] = (i+1)**2

print(result)