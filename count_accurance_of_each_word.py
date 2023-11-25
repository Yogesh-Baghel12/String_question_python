''' 
string= hello are a hello are a a
output= hello Present 2 Times
        are Present 2 Times
        a Present 3 Times
        hello Present 2 Times
        are Present 2 Times
        a Present 3 Times
        a Present 3 Times
'''


str=input("Enter a string : ")
str=str.split()
i=0 

while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count+=1
    print(str[i],"Present", count, "Times")
    i+=1
