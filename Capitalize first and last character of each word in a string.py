str=input("Enter a string : ")
str=str.title()
str=str.split()
string=""
for i in str:
    string+=i[:-1]+i[-1].upper()+" "

print(string)