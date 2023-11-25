str=input("Enter a String: ")
st=str.split()
largest=smallest=st[0]
for i in range(len(st)):
    if len(largest)<len(st[i]):
        largest=st[i]
    if len(smallest)>len(st[i]):
        smallest=st[i]
print("The Smallest word is :",smallest)

print("The largest word is :",largest)