str="adfdfd13d15gffh20"

num=0
sum=0
for i in str:
    if i.isdigit():
       num=num*10+int(i)
    else:
        sum=sum+num
        num=0
print(sum+num) 