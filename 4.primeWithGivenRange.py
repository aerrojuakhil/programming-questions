

n1=int(input())
n2=int(input())
l=[]
for i in range(n1,n2):
    if i==2:
        l.append(i)
    elif i%2==0 or i==1:
        pass
    else:
        for j in range(3,int(pow(i,0.5)+1),2):
            if j!=i and i%j==0:
                break
        else:
            l.append(i)
                
print(l)
print(len(l))