numbers = list(range(0,110,10))
first = []

# for num in numbers:
#     s = num * 2.5
#     if s % 2 == 0:
#         first.append(int(s))

i = 0
while i < len(numbers):
    s = numbers[i] * 2.5
    if s % 2 == 0:
        first.append(int(s))
    i += 1
print(first)