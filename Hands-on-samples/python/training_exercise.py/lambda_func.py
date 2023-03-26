# def mul(num1=5, num2=20, num3=100):
#     return num1 + num2 + num3

res1 = lambda num1 = 5, num2 = 20, num3 = 100 : num1 + num2 + num3

print(res1())

bowl = ["cherries","orange","apple","melon","figs"]
# def salad(fruit):
#     if fruit in bowl:
#         print(fruit)
#     else:
#         print("not in bowl")

# res2 = lambda x : x + ' in bowl' if bowl.count(x)>=1 else x + ' not in the bowl'
res2 = lambda x : x if x in bowl else "not in bowl"

print(res2("apple"))
print(res2("melon"))
print(res2("mango"))

# def inside(num):
#     if num in list(range(10)):
#         return num**2
#     else:
#         print("outside")
res3 = lambda x : x**2 if x in range(10) else "ocmosdc"
# res3 = lambda x : x**2 if x in list(range(10)) else "outside"
print(res3(4))
print(res3(78))
print(res3(8))
print(res3(1))
print(res3(67))
