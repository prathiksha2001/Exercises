import re

# pattern = re.compile("^[a-zA-Z0-9]+$")  # b+ - one or more, b* - zero or more, b? - zero or one
pattern = re.compile("^[A-Z][a-z]+$")

sentence = input("Enter a word: ")

if(pattern.match(sentence)):
    print("ACCEPTED")
else: 
    print("NOT ACCEPTED")

