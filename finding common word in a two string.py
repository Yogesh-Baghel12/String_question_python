str=input("Enter a String : ")
str2=input("Enter a string2 : ")
a=str.split()
b=str2.split()
c=""
for i in a:
    if i in b:
        c+=i + " " 
print(c)