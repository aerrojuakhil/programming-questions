n=int(input())
k=0
for i in str(n):
    k+=pow(int(i),int(len(str(n))))
#print(k)
if k==n:
    print("Armstrong number")
else:
    print("Not a armstrong")