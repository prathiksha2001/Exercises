sentence = input("Enter a string: ")
count = 0
for char in sentence:
    if char.isspace():
        count += 1

print(len(sentence)-count)

print(len(sentence.replace(" ","")))