ls1 = [-12,2,3,4,5,4,3,2,6,7,8]
s1 = set(ls1)
print(max(s1))
print(min(s1))
s2 = ""
s = "The quick brown fox jumps over the lazy dog"
for i in s.lower():
    if ord(i)>= 97 and ord(i)<=122:
        s2+=i
print(s2)
# res  = s.replace(" ","")
# print(res)
if len(set(s2.lower()))==26:
    print("The string is a panagram")
else:
    print("The string isn't a panagram")


