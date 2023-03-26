word = input("Enter a input : ")
word = word.lower()
ls = [word.count('a'), word.count('e'), word.count('i'), word.count('o'), word.count('u')]

if ls.count(0) > 0 :
    print("Not Accepted")
else:
    print("Accepted")

if len(set(word.lower()).intersection('aeiou')) >= 5:
    print ("Accepted")
else:
    print("Not Accepted")