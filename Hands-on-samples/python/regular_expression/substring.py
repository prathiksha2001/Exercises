import re
text = 'Python exercises, PHP exercises, C# exercises'
print(re.search('exercises',text))

for i in re.finditer('exercises', text):
    print(i.span())

print(re.findall('exercises',text))
new_s = re.sub('exercises','practices',text)
print(new_s)
