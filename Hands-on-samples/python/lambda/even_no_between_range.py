
result = filter(lambda x : (x%2==0),(range(21)))
print(result)
print(list(result))

#Write a program which can map() to make a list whose elements are square of numbers
#  between 1 and 20 (both included).
output = map(lambda x : x**2, range(1,21))
print(list(output))