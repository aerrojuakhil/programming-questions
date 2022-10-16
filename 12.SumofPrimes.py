n=int(input())
l=[]

for i in range(1,n,2):
    if i==2:
        l.append(2)
    else:
        for j in range(3,int(pow(i,0.5)+1),2):
            if j!=i and i%j==0:
                break
        else:
            l.append(i)
print(len(l))
a=[]
for x in range(len(l)):
    for y in range(x+1,len(l)):
        if x!=y and l[x]+l[y]==n:
            a.append([l[x],l[y]])
print(a)

