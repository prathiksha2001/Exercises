sentence = input("Enter a string: ")
ls = sentence.split()

for word in ls:
    if len(word) % 2 == 0:
        print(word)

ls = ''.join(ls)
for i in ls:
    if(ls.count(i)==1):
        print(i)
        break

