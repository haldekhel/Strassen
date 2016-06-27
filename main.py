
aFile = open("A.txt", 'r+')
bFile = open("B.txt", 'r+')
aN = int(aFile.readline())
bN = int(bFile.readline())
def genMatrix(inFile, d):
    x, y = 0, 0
    newMatrix = [[0 for i in range(d)]for j in range(d)]

    for line in inFile:
        dataline = (line.split())
        for y in range(d):
            newMatrix[x][y] = float((dataline[y]))
            print(dataline[y])
        x += 1
    return newMatrix

# def productMatrix(matrixA, matrixB):
#    d = len(matrixA)
#    matrixC = [[0 for x in range(d)] for y in range(d)]
#     for i in range(d):
#         for j in range(d):


matrixA = (genMatrix(aFile, aN))
matrixB = (genMatrix(bFile, bN))

print(matrixA)
# iterate through rows of X
matrixC = [[0 for i in range(len(matrixA))]for j in range(len(matrixA))]

for i in range(len(matrixA)):
   # iterate through columns of Y
   for j in range(len(matrixB)):
       # iterate through rows of Y
        for k in range(len(matrixB)):
            matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
