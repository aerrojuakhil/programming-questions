n = "Move-Hyphens-to-Front"
#n = str(input())
k = n.split("-")
new=''
for i in range(len(k)-1):
    new+="-"
k.insert(0, new)
newString = "".join(k)
print(newString)
