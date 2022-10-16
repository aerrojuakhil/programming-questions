n=int(input())
l=[]
for i in range(1,(n//2)+1):
    if n%i==0:
        l.append(i)
    else:
        pass
print(l)