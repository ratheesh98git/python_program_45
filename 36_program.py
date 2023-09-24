#36) Python program to add two matrices
l1=[[1,2,3],
    [4,5,6],
    [7,8,9]
    
    ]

l2=[[2,3,5],
    [4,6,7],
    [9,5,8]
    
    
    ]

result=[[0,0,0]
        ,[0,0,0]
        ,[0,0,0]]

for i in range(len(l1)):
    for j in range(len(l1[0])):
        result[i][j]=l1[i][j]+l2[i][j]
        
for row in result:
    print(row)
        
        