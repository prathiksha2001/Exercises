# x = 0
# case = []
# while x < 10:
#     s = "The number is " + str(x)
#     case.append(s)
#     x += 2
# print(case)

res = ["The number is "+ str(x) for x in range(0,10,2)]
print(res)