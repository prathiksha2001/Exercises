import re
import os

count = 0
res = []
print("\n")
for root, dirs, files in os.walk('D:/Hands-on-samples/python/'):
    print(root)
    for file in files:
        if file.endswith(".txt"):
            res.append(os.path.join(root, file))
# print(res)

# directory = 'D:/Hands-on-samples/python/'
# for file in os.listdir(directory):
#     if os.path.isfile(os.path.join(directory,file)):
#         count += 1
        
# print(count)


# with open('text.txt', 'r') as fp:
#     file_content = fp.readlines()
# print(file_content)
# for i , lines in enumerate(file_content):
#     file_content[i] = lines.replace('\n','')
# print(file_content)
# print(' '.join(file_content))




# import os
# import shutil

# source = "D:/Hands-on-samples/python/lambda/"
# destination = "D:/Hands-on-samples/python/"

# for filename in os.listdir(source):
#     source_file_address = source + filename
#     destination_file_address = destination + filename
#     shutil.copy(source_file_address, destination_file_address)

# print(os.listdir(destination))

# file_path = './text.txt'
# search_text = "hello"
# file_content = ""
# print(os.path.isfile(file_path))
# print(os.path.getsize(file_path))
# line_no = int(input("Enter line number: "))
# with open('./text.txt', 'r') as fp:
#     for line, line_content in enumerate(fp.readlines()):
#         if (line+1==line_no):
#             print(line_content)
#     if line_no > line:
#         print("doesn't exist")

# source = "D:/Hands-on-samples/python/lamda"
# destination = "D:/Hands-on-samples/python/files"
# os.replace(source, "D:/Hands-on-samples/python/lambda" )

# with open(file_path, 'r') as fp:
#     for line, line_content in enumerate(fp):
#         if search_text in line_content:
#             print(f"{search_text} exist at line number {line+1}")
#   #  print(line+1)
# print("")
# output = ""
# with open(file_path,'r') as fp:
#     ouput = fp.read()
# print(ouput)

# with open(file_path,'r') as fp:
#     ouput = fp.readlines()
# print(ouput)