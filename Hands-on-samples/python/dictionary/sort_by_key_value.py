dict1 = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

my_keys = list(dict1.keys())
my_keys.sort()

dict2 = { keys:dict1[keys] for keys in my_keys}
print(dict2)
