sentence = input("Enter a sentence: ")
ls1 = sentence.split()[::-1]
print(" ".join(ls1))

s = sentence.split()
# reversed() returns an iterator that yields characters from the input string in reverse order.
print(" ".join(reversed(s))) 