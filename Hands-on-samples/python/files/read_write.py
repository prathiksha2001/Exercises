content = ""
with open("text.txt", 'r') as fp:
    content = fp.read()

with open("rewrite.txt",'w') as fp:
    fp.write(content)