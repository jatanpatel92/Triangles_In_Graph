# This code is developed by Jatan Patel in order to be considered as a Software Engineer at Humanyze.

import sys

def getAdjMatrix(filePath):
    data = []
    for line in open(filePath,'r'):
        row = [int(x) for x in line.split(",")]
        data.append(row)
    return data

    
def brute_force(adjMatrix):
    computations = 0
    triangle = 0
    i = 0
    while i<len(adjMatrix[0]):
        j = i+1
        computations = computations+1
        while j<len(adjMatrix[0]):
            computations = computations+1
            if adjMatrix[i][j]==1:
                k = j+1
                while k<len(adjMatrix[0]):
                    computations = computations+1
                    if adjMatrix[i][k]==1 and adjMatrix[j][k]==1:
                        triangle = triangle+1
                    k = k+1
            j = j+1
        i = i+1
    return [triangle, computations]
    
def matrixMultiMethod(adjMatrix):
    adjMatrix_2 = matrix_multiply(adjMatrix, adjMatrix)
    adjMatrix_3 = matrix_multiply(adjMatrix, adjMatrix_2)
    trace = 0
    for i in range(len(adjMatrix_3[0])):
        trace+=adjMatrix_3[i][i]
    computations = 2*(len(adjMatrix_3[0])**3)+len(adjMatrix_3[0])
    return [trace/6, computations]

def matrix_multiply(x,y):
    m = len(x[0])
    n = len(y)
    z = [[0 for a in range(m)] for b in range(n)]
    i = 0
    while i<m:
        j = 0
        while j<m:
            k = 0
            while k<n:
                z[i][j] += x[i][k]*y[k][j]
                k+=1
            j+=1
        i+=1
    return z

def run():
    adjMatrix = getAdjMatrix(sys.argv[1])
    print "Number of vertices = "+str(len(adjMatrix[0]))
    print "==========================="
    print "Applying Brute Force Method"
    print "==========================="
    analysis = brute_force(adjMatrix)
    print "Number of triangles = "+str(analysis[0])
    print "Total number of computations (complexity) = "+str(analysis[1])
    print "==============================================="
    print "Applying Matrix Multiplication and Trace Method"
    print "==============================================="
    analysis = matrixMultiMethod(adjMatrix)
    print "Number of triangles = "+str(analysis[0])
    print "Total number of computations (complexity) = "+str(analysis[1])

if __name__ == '__main__':
    run()