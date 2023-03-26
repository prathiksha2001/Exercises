sentence = input("Enter a sentence: ")
pos = int(input("Enter a position that going to be deleted: "))
new_sentence = ""

for i in range(len(sentence)):
    if i == pos:
        continue
    new_sentence += sentence[i]

print(new_sentence)
print(sentence.replace(sentence[pos],''))

res = ''.join([sentence[i] for i in range(len(sentence)) if i!=pos ])
print(res)
    
