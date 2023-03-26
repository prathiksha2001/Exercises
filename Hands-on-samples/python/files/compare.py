d = open("rain.txt", "w")
d.write("Hi")
d.write("\nfood is hot"*2)
d.write("\nsunny day"*4)
d.close()

e = open("cloud.txt","w")
e.write("Hi")
e.write("\nfood is cold"*2)
e.write("\nsunny day"*4)
e.close()


d = open("rain.txt","r")
d_list = d.readlines()
d.close()
e = open("cloud.txt", "r")
e_list= e.readlines()
e.close()

for i in range(len(d_list)):
    print(d_list[i]==e_list[i])




