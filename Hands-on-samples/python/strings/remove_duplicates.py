word = input("Enter a input: ")

print("".join(set(word)))
#print(set(word))

unique = ""
for i in word:
    if i in unique:
        pass
    else:
        unique += i

print(unique)