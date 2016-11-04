# This code is developed by Jatan Patel in order to be considered as a Software Engineer at Humanyze.

import sys

def getAdjMatrix(filePath):
    data = []
    for line in open(filePath,'r'):
        row = [int(x) for x in line.split(",")]
        data.append(row)
    return data

def brute_force(adjMatrix):
    triangle = 0
    i = 0
    while i<len(adjMatrix[0]):
        j = i+1
        while j<len(adjMatrix[0]):
            if adjMatrix[i][j]==1:
                k = j+1
                while k<len(adjMatrix[0]):
                    if adjMatrix[i][k]==1 and adjMatrix[j][k]==1:
                        triangle = triangle+1
                    k = k+1
            j = j+1
        i = i+1
    return triangle
            
    
def run():
    adjMatrix = getAdjMatrix(sys.argv[1])
    print brute_force(adjMatrix)
    #print adjMatrix
    
    
if __name__ == '__main__':
    run()