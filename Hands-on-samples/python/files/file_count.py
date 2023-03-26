upper_count = 0
lower_count = 0
special_count = 0
digit = 0

with open("text.txt", "r") as file1:    
    file_content = file1.read() 
    #print(file_content)   
    for i in file_content:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
        elif i.isdigit():
            digit += 1
        else:
            special_count += 1
            # print(i)
    

print(upper_count,lower_count,digit,special_count)

    
# print(read_content)
#     

# print(upper_count)