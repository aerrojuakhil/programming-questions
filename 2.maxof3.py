a=int(input())
b=int(input())
c=int(input())

#Method 1
if a>= b and c:
    print(a)
elif b>= a and c:
    print(b)
elif c>= a and b:
    print(c)
#method 2
print(max(a,b,c))