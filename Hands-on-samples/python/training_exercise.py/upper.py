str1 = "Hello World PrograM"
count = 0
for i in str1:
    if i.isupper():
        count += 1
print(count)

# print(dir(str1[0]))

print(sum([1 for i in str1 if i.isupper()]))