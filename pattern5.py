# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
k=[]
a=[]
x=[]
y=[]
r=''
for i in range(1,(n+1)): #1 2 3 4 5
    L=[]
    
    for j in range(1,i+1): #1 2 3 4
        L.append(j)
    k.append(L)
    #print()
    m=[]
    for b in reversed(range(1,i)):
        m.append(b)
    a.append(m)

for i in k:
    i=''.join(map(str,i))
    x.append(i)
for j in a:
    j=''.join(map(str,j))
    y.append(j)
for i in range(len(x)):
    r+=(x[i]+y[i])+'\n'
print(r)
       
