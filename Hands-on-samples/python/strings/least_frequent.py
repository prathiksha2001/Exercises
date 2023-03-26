word = input("enter a word: ")
min_value = ''
max_value  = ''
min_count = len(word)
max_count = 0

# for i in word.split()
for i in word:
    if word.count(i) < min_count:
        min_count = word.count(i)
        min_value = i
    elif word.count(i) > max_count:
        max_count = word.count(i)
        max_value = i
        print(i)
        

print(min_value,min_count,max_value,max_count)

