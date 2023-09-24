#37) Python program to transpose a Matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


n1=len(matrix)
n2=len(matrix[0])

transpose_matrix=[]

for  j in range(n2):
    new=[]
    for i in range(n1):
        new.append(matrix[i][j])
    transpose_matrix.append(new)
        
print("this is  original matrix")

for x in matrix:
    print(x)
    
print("transpose matrix")

for t in transpose_matrix:
    print(t)