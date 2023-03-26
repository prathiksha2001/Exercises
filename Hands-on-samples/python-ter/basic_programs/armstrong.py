num = input("enter a number: ")

ls = list(num)
length = len(ls)
sum = 0
for i in ls:
   sum += int(i) ** length

print(sum)
if(sum == int(num)):
   print("Armstrong number")
else:
   print("not")


#string to list of integer
n = '154567'
ls = list(map(int,n))
print(ls)
