questions = [(10,4),(50, 5),(90, 10),("c", ("a","b","c")), (100, 100 )]

print(questions)

print((10,4) in questions)
print("c" == questions[3][0])
print("c" != questions[3][1][2])
print(50 in questions[1])
print(100 not in questions[4])