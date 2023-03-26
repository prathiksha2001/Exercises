def switch(operator):
    if operator == 8:
        return
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))

    if operator == 1:
        return num1*num2
    elif operator == 2:
        return num1 ** num2
    elif operator == 3:
        return num1/num2
    elif operator == 4:
        return num1//num2
    elif operator == 5:
        return num1%num2
    elif operator == 6:
        return num1+num2
    elif operator == 7:
        return num1-num2       

operator = 0
while(operator != 8):
    print("\n 1) multiplication \n 2) power\n 3)division\n 4) floor division\n 5) modulus\n 6) add \n7) sub \n 8) quit\n")
    operator = int(input("enter an operation: "))
    print(switch(operator))
 