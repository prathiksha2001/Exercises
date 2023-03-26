month =int(input("Enter a month: "))
year = int(input("Enter a year "))
list_31days = [1,3,5,7,8,10,12]

if month in list_31days:
    print("31")
else:
    if month == 2:
        if((year%4 == 0 and year%400==0) or (year%4==0 and year%100!=0)):
            print("29")
        else:
            print("28")
    else:
        print("30")
