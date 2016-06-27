import numpy as np

aFile = open("A.txt", 'r+')
bFile = open("B.txt", 'r+')
aN = int(aFile.readline())
bN = int(bFile.readline())

A = list[]
B = list[]
for x in xrange(aN):
    A = map()