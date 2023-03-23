matrixA = [[1,2,3],
           [4,5,6],
           [7,8,9]
          ]

matrixB = [[1,1,1],
           [1,1,1],
           [1,1,1]
          ]

row1 = len(matrixA)
row2 = len(matrixB)
col1 = len(matrixA[0])
col2 = len(matrixB[0])

if row1 == row2 and col1 == col2:
    result = []
    for i in range(row1):
        row_result = []
        for j in range(col1):
            row_result.append(matrixA[i][j] + matrixB[i][j])
        result.append(row_result)

    print(f"result of matrixA + matrixB is : {result}")

else:
    print("Matrix don't match")