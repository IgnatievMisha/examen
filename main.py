a=input()
b=a.split(" ")
print(b)
c=[]
for i in b:
    if int(i)%2==0:
        c.append(i)
print(c)