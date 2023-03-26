import re
 
phn = "612-555-1211"
# regex = re.compile("[6-9][0-9]{2}-[0-9]{3}-[0-9]{4}")
regex = re.compile('[6-9][0-9]{2}-[0-9]{3}-[0-9]{4}')
if re.match(regex, phn):
    print("Valid phone number")
else:
    print("Invalid phone number!")



# import re
# def find_valid_phone(text):
#     regex = re.compile('[\(\)]')
#     res = re.sub(regex,'',text)
#     return res

# print(find_valid_phone('Call me at 415-555-1011 tomorrow.'))
# print(find_valid_phone('My number is (212)-543-2212 tomorrow.'))

# import re
# def find_valid_phone(text):
#     regex = re.compile('(\d{3}|\(\d{3}\))-\d{3}-\d{4}')
#     return re.search(regex,text)

# print(find_valid_phone('Call me at 415-555-1011 tomorrow.'))
# print(find_valid_phone('My number is (212)-543-2212 tomorrow.'))
