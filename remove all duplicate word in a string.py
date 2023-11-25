str=input("Enter a string : ")
st=""
s=[]
for i in str:
    if i not in s:
        s.append(i)
str=""
for i in s:
    str+=i
print(str)
    