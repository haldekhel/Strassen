import numpy as np
import sys
arg1 = sys.argv[1]
arg2 = sys.argv[2]
aFile = open(arg1, 'r+')
bFile = open(arg2, 'r+')
aN = int(aFile.readline())
bN = int(bFile.readline())
counter = 0

def genMatrix(inFile, d):
    datalines = inFile
    newMatrix = []

    for x in range(0,d):
        dataline = datalines.readline().split()
        for y in range(0,d):
            yVals = list(map(float, dataline))

        newMatrix.append(yVals)
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
    n1 = len(mA)
    n2 = len(mB)
    global aN
    if(n1 and n2 <= aN):
        return (mA * mB)
    else:
        print(mA)
        A = partitionMatrix(mA)
        B = partitionMatrix(mB)
        mc = np.matrix([0 for i in range(len(mA))]for j in range(len(mB)))
        C = partitionMatrix(mc)


        a11 = np.array(A[0])
        a12 = np.array(A[2])
        a21 = np.array(A[1])
        a22 = np.array(A[3])

        b11 = np.array(B[0])
        b12 = np.array(B[2])
        b21 = np.array(B[1])
        b22 = np.array(B[3])

        mone = np.array(strassen((a11 + a22), (b11 + b22)))
        mtwo = np.array(strassen((a21 + a22), b11))
        mthree = np.array(strassen(a11, (b12 - b22)))
        mfour = np.array(strassen(a22, (b21 - b11)))
        mfive = np.array(strassen((a11 + a12), b22))
        msix = np.array(strassen((a21 - a11), (b11 + b12)))
        mseven = np.array(strassen((a12 - a22), (b21 + b22)))

        C[0] = np.array((mone + mfour - mfive + mseven))
        C[2] = np.array((mthree + mfive))
        C[1] = np.array((mtwo + mfour))
        C[3] = np.array((mone - mtwo + mthree + msix))

        return np.array(C)

matrixA = genMatrix(aFile, aN)
matrixB = genMatrix(bFile, bN)
matrixA = np.matrix(matrixA)
matrixB = np.matrix(matrixB)

matrixC = [[0 for i in range(len(matrixA))]for j in range(len(matrixA))]

print("C =")
print(strassen(matrixA, matrixB))

