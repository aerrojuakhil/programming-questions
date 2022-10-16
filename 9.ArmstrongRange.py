n1=int(input())
n2=int(input())
l=[]
for i in range(n1,n2):
    k=0
    for a in str(i):
        k+=pow(int(a),len(str(i)))
    if k==i:
        l.append(i)
print(l)
