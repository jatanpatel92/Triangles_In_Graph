import sys

p = 0
mapper = {}
def getAdjMatrix(filePath):
    data = []
    for line in open(filePath,'r'):
        row = [int(x) for x in line.split(",")]
        data.append(row)
    return data

def set_num_of_partitions(n):
    return n/10

def getHash(i):
    global p
    return int(i/p)


def issSubSet(i, j, x, y, z):
    if (i==x and j==y) or (i==y and j==x) or (i==y and j==z) or (i==z and j==y) or (i==x and j==z) or (i==z and j==x):
        return True
    return False

def isSubSet(i, j, x, y):
    if (i==x and j==y) or (i==y and j==x):
        return True
    return False

def map_function(i, j):
    global p
    global mapper
    part_i = getHash(i)
    part_j = getHash(j)
    #if part_i == part_j:
    x=0
    while x<p-2:
        y=x+1
        while y<p-1:
            if isSubSet(part_i, part_j, x, y):
                if mapper.has_key(str(x)+str(y)):
                    mapper[str(x)+","+str(y)].append(str(i)+","+str(j))
                else:
                    mapper.update({str(x)+","+str(y):[str(i)+","+str(j)]})
            y+=1
        x+=1
    #else:
    if part_i != part_j:
        x=0
        while x<p-3:
            y=x+1
            while y<p-2:
                z=y+1
                while z<p-1:
                    if issSubSet(part_i, part_j, x, y, z):
                        if mapper.has_key(str(x)+","+str(y)+","+str(z)):
                            mapper[str(x)+","+str(y)+","+str(z)].append(str(i)+","+str(j))
                        else:
                            mapper.update({str(x)+","+str(y)+","+str(z):[str(i)+","+str(j)]})
                        #print mapper
                    z+=1
                y+=1
            x+=1
        

def brute_force(adjMatrix):
    triangle = []
    i = 0
    while i<len(adjMatrix[0]):
        j = i+1
        while j<len(adjMatrix[0]):
            if adjMatrix[i][j]==1:
                k = j+1
                while k<len(adjMatrix[0]):
                    if adjMatrix[i][k]==1 and adjMatrix[j][k]==1:
                        triangle.append(str(i)+","+str(j)+","+str(k))
                    k = k+1
            j = j+1
        i = i+1
    return triangle


def reduce_function(n):
    global p
    global mapper
    triangles = []
    count = 0
    #count triangles
    for key, values in mapper.viewitems():
        if len(values)>2:
            sub_graph = [[0 for i in range(n)] for j in range(n)]
            for s in values:
                s = [int(x) for x in s.split(",")]
                sub_graph[s[0]][s[1]] = 1
                sub_graph[s[1]][s[0]] = 1
            t = brute_force(sub_graph)
            if len(t)>0:
                triangles.append(t)
    print len(triangles)
    for t in triangles:
        t = [int(x) for x in t[0].split(",")]
        if (getHash(t[0]) == getHash(t[1])) and (getHash(t[1]) == getHash(t[2])):
            count += 1/(p-1)
        else:
            count += 1
    print count
    
def run():
    global p
    adjMatrix = getAdjMatrix(sys.argv[1])
    n = len(adjMatrix[0])
    p = set_num_of_partitions(n)
    i = 0
    while i<n-1:
        j = i+1
        while j<n:
            if adjMatrix[i][j]==1:
                map_function(i, j)
            j+=1
        i+=1
    #print mapper
    reduce_function(n)
if __name__ == '__main__':
    run()