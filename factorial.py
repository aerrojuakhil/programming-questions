def fact(a):

    if a == 0:
        return 1
    return a * fact(a-1)
k= fact(5)
print(k)