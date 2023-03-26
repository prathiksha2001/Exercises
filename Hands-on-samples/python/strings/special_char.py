import re
sentence = input("enter a sentence: ")

print(re.findall(r"[!@#$%&]",sentence))
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')     
     
if(regex.search(sentence) == None):
        print("String is accepted")
         
else:
    print("String is not accepted.")
    