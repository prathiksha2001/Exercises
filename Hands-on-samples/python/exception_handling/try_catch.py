# try:
#    n =  int(input("enter a number between 1 to 10: "))
#    print(n)
#    assert n <= 10
# except AssertionError:
#    print("input should be less than 10 :) ")
# else:
#     print('hi')
# finally:
#    print("completed")

dict1 = {'name': 'prathiksha', 'address':'10 orange land'}
try:
   key = input("enter a key: ")
   print(dict1[key])
except KeyError:
    print('key not found :) ')
finally:
   print('completed')