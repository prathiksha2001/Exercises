text = "ABCDEFCHIJKLMNOPQRSTUVWXYZ"
res = ""

for i in text:
    res += chr((ord(i) + ord('A') + 3)%26 + ord('A'))

print(res)
# for i in text:
#    res += chr((ord(i)-ord('A') + 3) % 26 + ord('A')) 

# print(res)
print(ord('A'))
print(chr(120))