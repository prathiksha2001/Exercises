word = input("Enter a word: ")
mid_length = int(len(word)/2)
#print(mid_length)
new_word = word[:mid_length] + word[mid_length:].upper()
print(new_word)