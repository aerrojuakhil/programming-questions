n= int(input())

''' Method 1
for i in range(2,n):
    if n!=i and n%i==0 or n==1:
        print("Not prime")
        break
    elif n==2:
        print("prime")
    else:
        print("prime")
        break'''
        
#reduces time complexity
if n%2==0:
    print("Not Prime")
elif n==2:
    print("prime")
else:
    for i in range(3,int(pow(n,0.5)+1),2): #range-> 3 5 7 9
        if n!=i and n%i==0 or n==1:
            print("Not prime")
            break
        else:
            print("prime")
            break