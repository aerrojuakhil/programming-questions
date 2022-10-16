# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
k=''
r=''
for i in range(1,n):
    k=''
    for j in range(i):
        k+="%s"%i
    r+=k+'\n'
print(r)
        