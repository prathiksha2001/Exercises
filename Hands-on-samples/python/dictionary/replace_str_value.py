import re
test_str = 'geekforgeeks best for geeks'
repl_dict = {"geeks" : "all CS aspirants", "for" : "Hello World"}
res = ""
# for i in repl_dict.keys():
#     print(i)
#     res = re.sub(i,repl_dict[i],test_str)
# print(res)

res = test_str
for i in repl_dict.keys():
    print(i)
    test_str = re.sub(i,repl_dict[i],test_str)

print(test_str)
# res = "hello"
# #res[2] = 's'
# print(res)