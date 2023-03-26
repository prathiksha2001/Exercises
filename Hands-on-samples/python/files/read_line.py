
with open('text.txt','r') as fp:
    with open('output.txt', 'w') as op:
        op.write(fp.read().upper())

with open('output.txt','r+') as fp:
    content = fp.read().title()
    



# match = input("Enter  string: ")

# file = open("text.txt",'r')

# for  i , line in enumerate(file):
#     if line.count(match) >= 1:
#         print(line)



# content = []
# with open('files//temp.txt','r') as fp:
#     content = fp.readlines()

# # print(content[int(input("enter a index: "))])

# x = int(input("enter a index: "))
# y = [0,3]
# fp = open('files//temp.txt','r')

# for i,line in enumerate(fp):
#     if i in y:
#         print(line)