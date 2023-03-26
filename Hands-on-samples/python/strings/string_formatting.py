name = "bob"
grade = "A+"

print("the student's name is {} and the grade is {}".format(name, grade))

animals = ["lions", "zebras", "elephants"]
safari = "I saw {}, {} and {}!"
print(safari.format(animals[0].upper(),\
    animals[1].capitalize(),animals[2].upper()))
print(safari.format(*animals))

numbers = [10,20,30,40]
print(eval("100+2"))
print(eval("{} + {} + {}+ {}".format(*numbers)))
print(sum(numbers))
print(eval("{0} + {0} + {0}+ {0}".\
           format(*numbers))) 
num = 300/9
print(f"days left are {num: .2f}")