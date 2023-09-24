#38) Python program to multiply Two Matrices


l1=[[1,2,3],
    [4,5,6],
    [7,8,9]
    ]
l2=[[2,3,4],
    [4,5,6],
    [7,8,9]
    
    ]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]
        
        ]

for i in range(len(l1)):
    for j in range(len(l1[0])):
        result[i][j]=l1[i][j]*l2[i][j]
        
print("this is result")

for  row in result:
    print(row)