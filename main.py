dict={}
lst=[]
for i in range(3):
    name=input()
    mark=int(input())
    dict[name]=mark
    lst.append(dict[name])
    lst.append(mark)
    x=max(lst)
    print(dict)
for key, value in dict:
    if value==x:
        print(key)