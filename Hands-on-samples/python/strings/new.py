n="This is a python language"

# for i in range(1,len(n),2):
#     print(n[i],end=" ")
for i , word in enumerate(n.split()):
    if i%2 == 1:
        print(word,end=" ")

# for i in range(0,len(n),2):
#     print(n[i], end="")
   
# for word in n.split():
#     if len(word)%2 == 0:
#         print(word)

# result = input().split(',')
# print(result)