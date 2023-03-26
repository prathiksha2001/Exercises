count = 0
with open("rewrite.txt",'r') as fh:
    count += sum(1 for line in fh for character in line if character.isupper())

print(count)