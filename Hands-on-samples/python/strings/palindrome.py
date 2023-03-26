sentence = input("Enter a input: ")

print(sentence == sentence[::-1])

end = len(sentence)-1
start = 0
palindrom = True

while start < end:
    for i in range(len(sentence)):
        if sentence[i] != sentence[end]:
            palindrom = False
            break
        end -= 1
    if(not palindrom):
        break
    
        

print(palindrom)
    

