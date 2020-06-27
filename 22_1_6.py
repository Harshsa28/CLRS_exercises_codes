from numpy import matrix
x = matrix([[0,1,1,0], [1,0,1,0],[0,0,0,0], [0,0,1,1]])
def universal_sink(matrix):
    i = 0 
    j = 0
    while (i != len(matrix) and j != len(matrix)):
        if matrix[i,j] == 0:
            j += 1
        else:
            i += 1
    for k in range(len(matrix)):
        if matrix[i,k] != 0:
            print("no universal sink")
            return
    for k in range(len(matrix)):
        if matrix[k,i] != 1:
            if k != i:
                print("no universal sink")
                return
    print("universal sink is :", (i+1))

universal_sink(x)
