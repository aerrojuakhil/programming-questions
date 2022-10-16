n=int(input())
'''
l=[]
for i in str(n):
    l.append(i)
print(l)

for i in range(len(l)):
    if l[i]==l[len(l)-i-1]:
        k="Palindrome"
    else:
        k="Not palindromr"
        break
print(k)'''
#method 2

reverse= int(str(n)[::-1])

if n==int(reverse):
    print("palindrome")
else:
    print("Not a palindrome")
