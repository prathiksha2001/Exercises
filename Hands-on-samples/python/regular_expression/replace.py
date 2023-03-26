name = "prathikshaaaaaaaaaaa"
print(name.replace('a','A',5))

string = "Favtutor Blog: How to Remove multiple characters in a string in Python"
print("Original string: ", string)
to_remov = {"t": "T", "l": "L", "r": "R", "s": "S"}

for key,value in to_remov.items():
    string = string.replace(key,value)
    
print(string)


import re
re_len = re.compile('.{8}')
re_upper = re.compile('.*[A-Z]+')
re_lower = re.compile('.*[a-z]+')
re_digit = re.compile('.*[0-9]+')
re_special = re.compile('.*[\[\],\*!@#$%\^&\(\)\\><\|"]+')
def password_verify(password):
    if(re.search(re_len,password)==None):
        print("password length must be greater than or equal to 8")
    elif(re.search(re_lower,password)==None):
        print("password must have atleast one lowercase letter")
    elif(re.search(re_upper,password)==None):
        print("password must have atleast one uppercase letter")
    elif(re.search(re_digit,password)==None):
        print("password must have atleast one digit")
    elif(re.search(re_special,password)==None):
        print("password must have atleast one special character")
    else:
        print("STRONG PASSWORD")
password_verify("Ps]sssssa1")
