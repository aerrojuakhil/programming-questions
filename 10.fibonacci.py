n=int(input())
b=1
a=0
print(a,b,end=" ")
for i in range(2,n): # 0 1 2 3 4 5 6
    z=a+b
    a=b
    b=z
    print(z,end=" ")

