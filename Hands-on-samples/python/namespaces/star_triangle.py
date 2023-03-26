# for i in range(1,6):
#     for j in range(i):
#         print('*' ,end="")
#     print('\n')

def pyramid(n):
    for i in range(n):
        print(' '*(n-i-1)+'*'*(2*i+1))
    print('\n')

pyramid(3)

for i in range(1,6):    
    print('*'*i,end="\n")
# print('----------------------------------------')
for i in range(6,0,-1):
    print('*'*i,end="\n")
print('\n')
n = 6
for i in range(0,n):
    print(' '*i + '*'*(n-i))
n = 7
for i in range(1,n):
    print(" "*(n-i-1)+'*'*(i))

