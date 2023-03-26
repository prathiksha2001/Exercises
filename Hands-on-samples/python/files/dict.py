import json 
import os

word = ''
with open('text.txt', 'r') as fp:
    word = fp.read()
    
result = word.replace('\n',' ').split()
print(max(result, key=len))
print(max(result, key=result.count))
print(max(result, key=result.index))

# detail = { "name" : "prathiksha", "age" : 20}

# with open('files//dictionary_file.txt', 'w') as file:
#     json.dump(detail,file)
    

# print(os.path.isfile('dictionary_file.txt'))
# print(os.path.getsize('dictionary_file.txt'))