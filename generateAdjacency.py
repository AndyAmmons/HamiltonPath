import numpy as np



#generate random adjacency list for a graph of n nodes

def GenerateAdj(n = 20):
    
    adj = []
    for j in range(2):
        for i in range(n):
            newEdge = sorted([i,getRandom(i,n)])
            if newEdge not in adj:
                adj.append(newEdge)

    return adj

def getRandom(i,n):
    
    rando = np.random.randint(n)
    while rando == i:
        rando = np.random.randint(n)
    return rando

def transAdjacency(adj):
    nodes = [[]]
    nadj = list.copy(adj)
    

    for i in range(len(nadj)):
        for index, j in enumerate(nadj):
            if i in j and i != j:
                nodes[i].append(index)
                
        if i < len(nadj)-1:
            nodes.append([])
    #print(nodes)
    return nodes


def reduceTransAdj(tadj):

    rTadj = [i[:] for i in tadj]
    #nodes=[[]]

    for edge in range(len(rTadj)):
        if len(rTadj[edge]) > 2:
            found = False
            for node in rTadj[edge]:
                for index, newedge in enumerate(rTadj):
                    if len(newedge) > 1 and edge != index and len(rTadj[edge]) > 2:
                        if node in newedge:
                            newedge.remove(node)
                            found = True
                if (found and len(rTadj[edge]) > 2):
                    rTadj[edge].remove(node)
                
                #elif (not found and len(redTadj[edge]) > 2):
                    #redTadj[edge].remove(node)
        else:
            pass
    for edge in rTadj:
        if len(edge) == 1:
            edge += [edge[0]]
    return rTadj

def getDegrees(redTadj,n = 20):
    deg = [0]*len(redTadj)
    for i in range(n):
        #print(deg)
        if len(redTadj[i]) == 1:
            deg[redTadj[i][0]] += 2
        elif len(redTadj[i]) > 2:
                deg[redTadj[i][0]] += (deg[redTadj[i][0]]*2 + 1)
                deg[redTadj[i][1]] += (deg[redTadj[i][0]]*2 + 1)
                deg[redTadj[i][2]] += (deg[redTadj[i][0]]*2 + 1)
        else:
            deg[redTadj[i][0]] += 1
            deg[redTadj[i][1]] += 1
            
    return deg
                        
def printEdges():
    adj = GenerateAdj(n = 10)
    print('Adjacency list: ',adj)
    tadj = transAdjacency(adj)
    print('Transformed: ',tadj)
    rtadj = reduceTransAdj(tadj)
    print('Reduced: ',rtadj)

    return adj, tadj, rtadj
'''
def reconnect(adj,rtadj):
    for i in rtadj:
        if len(i) == 1:
            for j in rtadj:
                if (adj[i][0] in adj[j] or adj[i][1] in adj[j]) and len(j) == 1:
                    rtadj += [[i,j]]
                    rtadj.remove(j)
                elif (adj[i][0] in adj[j] or adj[i][1] in adj[j]) and len(j) == 2:
                    
                    
'''   


if __name__ == '__main__':
    adj,tadj,rtadj = printEdges()
    #printEdges()
    #getDegrees(rtadj)
    print('in generateAdjacency.py')
    
    #mygraph

    


    

