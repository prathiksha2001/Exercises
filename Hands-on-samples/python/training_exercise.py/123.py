my_str = "Hello!!!, he said ---and went to () this place @all #me ."
new_str = ""

import re
pattern = re.compile("[!,-.@#$%^&*)()]")
print(re.subn(pattern,"",my_str))
# print(len(my_str))
# for str in my_str:
#     if str == '!' or str == "," or str == "-" or str =='.':
#         continue
#     else:
#         new_str = new_str + str
   
# print(new_str)

# import re

# print(re.sub(r"\!*\,*\-*\.*","",my_str))

# pattern = re.compile('[a-z]')
# print(re.sub(pattern,"",my_str))
ip = 'This note should not be NoTeD'
print(re.sub("note","X",ip,flags=re.I))

para = '''\
(mall) call ball pall
ball fall wall tall
mall call ball pall
wall mall ball fall
mallet wallet malls
mall:call:ball:pall'''
ls =  para.split('\n')
for line in ls:
    print(re.sub(r'^mall\b','1234',line))


items = ['lovely', '1\ndentist', '2 lonely', 'eden', 'fly\nfar', 'dent']
print([i for i in items if re.search('(^den|ly$)',i)])

