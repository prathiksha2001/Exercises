sentence = input("enter a string: ")
vowel = "aeiou"
count = 0;
for char in sentence.lower():
    if char in vowel:
        count += 1

print(count)
