sentence = input("Enter a string: ")
max_len = 0 #= [0,'']
char = ''

for i in sentence:
    if(sentence.count(i)>max_len):
        max_len = sentence.count(i)
        max_len_char = i

print(max_len_char, '-', max_len)


# for character in sentence:
#     if sentence.count(character) > max_len[0]:
#         max_len[0] = sentence.count(character)
#         max_len[1] = character

# print(max_len[1], max_len[0])