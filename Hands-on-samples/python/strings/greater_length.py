sentence = input("Enter a sentence: ")
length = int(input("Enter the length: "))
words = sentence.split()
output = ""
for word in words:
    if(len(word) >= length):
        output += word + " "

print(output)
print(len(output.strip()))

