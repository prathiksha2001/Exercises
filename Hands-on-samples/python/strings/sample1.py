robot = "technologically"

consoles = "ps4 is cooler than xbox!"

code = "ply2t3h4o5n6i7c8"

words = "I saw a cat jump over the moon and into the clouds"

new_words = "I saw a cow fly over the gates and into the forest"

paid = "I received a total of $5000"

print(len(robot))
print(robot[:6]) #slicing
print(robot[1]) #indexing
print(robot[6:])
print(robot[6:13])
print(robot[10:14])

#Operations on console 
print(consoles[-17:-11])
print(consoles.endswith("-"))
print(len(consoles))
print(consoles.find("x"))
print(consoles.find("x",10,19))
print(consoles.count("x"))
print(consoles[-1])

#operations on console
print(code)
print(code[0::2].upper())
print(code[1::2])
print(code[1::2][::-1])

#Operations on words
print(words)
var = words.split()
print(len(var))
print(var[3:])
print(var[3:10:2])

#operations on new_words
print(new_words)
sl = slice(3,12,2)
print(new_words.split()[sl])
print(new_words.split()[3:12:2])
print("cat" in var)
print(" ".join(var))

#operations on paid

print(paid)
print(paid.split("$")[1])