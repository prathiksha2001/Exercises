   
def sayHello():
    print("Hello")

def even(num=4):
    if(num%2==0):
        print("yes")
    else:
        print("no")
val = int(input("enter a number: "))
even(val)

if __name__ == '__main__':   
    sayHello()
