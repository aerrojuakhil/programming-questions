#Method 1
n=int(input())
if n%4==0:
    if n%100==0:
        if n%400==0:
            print("Leap")
        else:
            print("Non Leap")
    else:
        print("Leap")
else:
    print("Leap")
#Method2
n=int(input())
if (n%4==0 and n%100!=0) or n%400==0:
    print(n*n)
else:
    print(n*2)

