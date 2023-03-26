word = input("Enter a string: ")
res = []
for i in word:
    if(word.count(i)%2 == 1):
        res.append(i)

print(res)