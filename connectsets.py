import numpy as np
import unionfind as uf
from itertools import chain




def connectSets(adj, rtadj):
    InNodes = list(chain.from_iterable(rtadj)) # which nodes are involved?
    #find disjoint sets:
    union = uf.unionfind(10)

    for i in range(len(rtadj)):
        if len(rtadj[i]) == 1:
            for j,edge in enumerate(rtadj):
                if rtadj[i] in edge:
                    union.unite(i,j)
        elif len(rtadj[i]) == 2:
            for j,edge in enumerate(rtadj):
                if rtadj[i][0] in edge or rtadj[i][1] in edge:
                    union.unite(i,j)

    #gather pendants:
    pendants = [index for index, i in enumerate(rtadj) if len(i) == 1]

    #determine which sets the pendants appear in:
    groups = union.groups()
    PunionLoc = []

    for i in range(len(pendants)):
        for index, j in enumerate(groups):
            if pendants[i] in j:
                PunionLoc += [index]
    #isolate deg 1 node in pendant from set containing pendant
    freeNodes = []
    freeNeighbors = []

    for i in pendants:
        freenode = 0
        #freeNeighbor = 0
    
        for index,j in enumerate(groups):
        
            if index in PunionLoc:
                for k in j:
                    if adj[rtadj[i][0]][0] in adj[k] and i != k:
                        freenode = adj[rtadj[i][0]][1]
                        freeNeighbors += [adj[k]]
                        break
                    elif adj[rtadj[i][0]][1] in adj[k] and i != k:
                        freenode = adj[rtadj[i][0]][0]
                        freeNeighbors += [adj[k]]
                        break
        freeNodes += [freenode]

    # gather possible edges from query nodes in independent sets:

    PosEdges = []
    PosEdgeInd = []
    for i in freeNodes:
        for index,g in enumerate(groups):
            if index not in PunionLoc:
                for p in g:
                    Possible1 = [i,adj[p][0]]
                    Possible2 = [i,adj[p][1]]
                    if Possible1 not in PosEdges:
                        PosEdges += [Possible1]
                        PosEdgeInd += [p]
                    elif Possible2 not in PosEdges:
                        PosEdges += [Possible2]
                        PosEdgeInd += [p]

    # for possible edges: find one in adj not in rtadj, and return its index.
    found = 0
    newEdgeIndex = 0
    for i in PosEdges:
        for ind, newEdge in enumerate(adj):
            #print(i, newEdge)
            if (i[0] in newEdge and i[1] in newEdge) and (ind not in InNodes) and (freeNodes[0] in newEdge) != (freeNodes[1] in newEdge):
                found = 1
                newEdgeIndex = ind
                break
        if found == 1:
            break
   
    # find the connecting node in newEdge not in freeNodes:
    connNodeInd = 0
    midConnNode = 0
    for ind, node in enumerate(newEdge):
        for i in freeNodes:
            if node not in adj[i]:
                connNodeInd = ind
                midConnNode = node
                break

    #find the edge in pendants to connect to intermediate new edge:
    # connect new Edge node to that pendant.

    for i in pendants:
        if midConnNode in adj[rtadj[i][0]]:
            connNode = rtadj[i][0]
            rtadj[i] += [newEdgeIndex]
            break
    
    
    #need to find edges to delete and to connect.
    #connect up midConnNode to disconnected set:
    #connect new edge to rtadj:
    node2Del = 0
    for ind, g in enumerate(groups):
        if ind not in PunionLoc:
            for n in g:
                if midConnNode in adj[n]:
                    #connCandidates += rtadj[n]
                    delete = np.random.randint(1)
                    node2Del = rtadj[n].pop(delete)
                    rtadj[n] += [newEdgeIndex]
                
    for i in rtadj:
        if node2Del in i:
            i.remove(node2Del)

    return rtadj

if __name__ == '__main__':
    
    adj = [[0, 4], [1, 9], [2, 7], [3, 5], [4, 1], [5, 3], [6, 7], [7, 1], [8, 4], [9, 4], [0, 2], [1, 2], [2, 8], [3, 6], [4, 2], [5, 7], [6, 3], [7, 6], [8, 1], [9, 0]]
    rtadj = [[10, 19], [4], [10, 12], [5, 16], [4, 9], [5, 15], [16, 17], [15, 17], [12], [9, 19], [], [], [], [], [], [], [], [], [], []]

    newrtadj = connectSets(adj,rtadj)

                


            
        
