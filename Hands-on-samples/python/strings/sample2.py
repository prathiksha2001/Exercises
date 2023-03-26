toys = {"robot": "$40.0", "car":"$25", "ironman":"$12"}
values = list(toys.values())
print(values)
result = []
for value in values:
    result.append(value.split("$")[1])

res = eval("{}+{}+{}".format(*result))
print()
print(res)

num = int(eval(values[0][1:])+eval(values[1][1:])+eval(values[2][1:]))

print(num)