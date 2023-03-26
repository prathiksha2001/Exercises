a = 1
b = 1
print(a,b,end=" ")
for i in range(8):
    c = a+b
    a = b
    b = c
    print(c, end=" ")

def feb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return feb(n-1) + feb(n-2)

print(feb(10))