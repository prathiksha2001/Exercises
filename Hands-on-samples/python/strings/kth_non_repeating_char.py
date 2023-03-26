str = "geeksforgeeks" 
k = 3

non_repeating_characters = []

for i in str:
    if i in non_repeating_characters:
        non_repeating_characters.remove(i)
    elif i not in non_repeating_characters and str.count(i)==1:
        non_repeating_characters.append(i)  

print(non_repeating_characters[k-1])
# for char in str:
#     if str.count(char) == 1:
#         non_repeating_characters.append(char)

# print(non_repeating_characters[k-1])

# ls1 = list[range(0,10)]
# print(ls1)