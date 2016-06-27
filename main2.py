import numpy as np

aFile = open("A.txt", 'r+')
bFile = open("B.txt", 'r+')
aN = int(aFile.readline())
bN = int(bFile.readline())

counter = 0



def genMatrix(inFile, d):
    datalines = inFile
    x, y = 0, 0
    newMatrix = [[0 for i in range(d)]for j in range(d)]

    for x in range(0,d):
        dataline = datalines.readline().split()
        for y in range(0,d):
            newMatrix[x][y] = float(dataline[y])
            print (dataline)

    return newMatrix

def partitionMatrix(matrix):
    length = len(matrix)
    if(length % 2 is not 0):
        stack = []
        for x in range(length + 1):
            stack.append(float(0))
        length += 1
        matrix = np.insert(matrix, len(matrix), values=0, axis=1)
        matrix = np.vstack([matrix, stack])
    d = (length // 2)
    matrix = matrix.reshape(length, length)
    completedPartition = [matrix[:d, :d], matrix[d:, :d], matrix[:d, d:], matrix[d:, d:]]
    return completedPartition

def strassen(mA, mB):
    n = len(mA)
    global matrixC
    if(n == 1):
        return np.multiply(mA, mB)
    else:

        A = partitionMatrix(mA)
        B = partitionMatrix(mB)
        A[1], A[2] = A[2], A[1]
        B[1], B[2] = B[2], B[1]
        mc = np.matrix([0 for i in range(len(mA))]for j in range(len(mB)))
        C = partitionMatrix(mc)

        mone = strassen(np.add(A[0], A[3]), np.add(B[0], B[3]))
        mtwo = strassen(np.add(A[1], A[3]), B[0])
        mthree = strassen(A[0], np.subtract(B[2], B[3]))
        mfour = strassen(A[3], np.subtract(B[1], B[0]))
        mfive = strassen(np.add(A[0], A[2]), B[3])
        msix = strassen(np.subtract(A[1], A[0]), np.add(B[0], B[2]))
        mseven = strassen(np.subtract(A[2], A[3]), np.add(B[1], B[3]))


        C[0] = np.subtract(np.add(mone, mfour), np.add(mfive, mseven))
        C[2] = np.add(mthree, mfive)
        C[1] = np.add(mtwo, mfour)
        C[3] = np.add(np.subtract(mone, mtwo), np.add(mthree, msix))

        return C

matrixA = np.matrix((genMatrix(aFile, aN)))
matrixB = np.matrix((genMatrix(bFile, bN)))

matrixC = [[0 for i in range(len(matrixA))]for j in range(len(matrixA))]

partitionedA = partitionMatrix(matrixA)
partitionedB = partitionMatrix(matrixB)

print(partitionMatrix(matrixA))

print(strassen(matrixA, matrixB))

