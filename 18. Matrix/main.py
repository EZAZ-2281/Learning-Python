matrix = [
    [1, 2, 3], 
    [4, 5, 6]
]
matrix[0][2] = 7
print(matrix[1][2])
print(matrix[0][2])

matrix2 = [
    [1, 2, 3], 
    [4, 5, 6]
]
for x in matrix2: 
    for y in x: 
        print(y) 