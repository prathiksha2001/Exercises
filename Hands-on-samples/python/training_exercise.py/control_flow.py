choose_dish = input("Enter a number 0 to 2: ")
pick_sauce = input("Enter a number 0 to 2: ")

cooked_pasta = ['hot', 'cold', 'over cooked']
sauce = ['spicy', 'sweet', 'savoury']

if eval(choose_dish) <= 2 or eval(pick_sauce) <= 2:
    print(f"My meal is {cooked_pasta[eval(choose_dish)]} and very {sauce[eval(pick_sauce)]} !")

print(eval(choose_dish))