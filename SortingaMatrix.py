
matrix=[[8,4,2],[1,2,3],[7,6,5]]
'''
# stores a sorted list/array in a different list

k=sorted(matrix,key=lambda x: x[1])
print(k)'''
'''
k=sorted(matrix,key=lambda x: x[1],reverse=True)
print(k)'''

'''
# sorts a list
matrix.sort(key=lambda x: x[1])
print(matrix)'''
'''
matrix.sort(key=lambda x: x[1],reverse=True)
print(matrix)'''
'''matrix.reverse()
print(matrix)'''


