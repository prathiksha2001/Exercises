num = int(input("enter a number: "))

if num < 0:
    print("no factorial found")
else:
    n = 1;
    i= 1
    while(i<=num):
        n *= i
        i += 1

    print(n)

    