def matrix_multiplication(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None

    res = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            sum = 0
            for k in range(len(matrix2)):
                sum += matrix1[i][k] * matrix2[k][j]
            row.append(sum)
        res.append(row)
    return res
                

def main():
    mat1 = [
        [7,14,15,6],
        [4,8,12,3],
        [14,21,6,9],
        [13,7,6,4]
    ]

    mat2 = [
        [5,7,14,2],
        [8,16,4,9],
        [13,6,8,4],
        [6,3,2,4]
    ]

    res = matrix_multiplication(mat1, mat2)

    for row in res:
        print(row)

main()


'''
[378, 381, 286, 224]
[258, 237, 190, 140]
[370, 497, 346, 277]
[223, 251, 266, 129]
'''