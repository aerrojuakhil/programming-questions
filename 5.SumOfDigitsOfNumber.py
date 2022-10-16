#from unicodedata import digit


n=int(input())
k=0
'''for i in str(n):
    k+=int(i)
print(k)'''

while n!=0:
	digit = int(n%10)
	k += digit
	n = n/10
print(k)