# connect pendants:
import findsets as fs
import numpy as np
from itertools import chain



def connectSingles(adj, rtadj,n=10):

    pendants = [index for index, i in enumerate(rtadj) if len(i) == 1]
    InNodes = list(chain.from_iterable(rtadj))
    groups = fs.findSets(rtadj,n)
    freeNodes = []

    for p1ind, p1 in enumerate(pendants):
        for p2ind,p2 in enumerate(pendants):
            if p1ind != p2ind:
                if adj[rtadj[p1][0]][0] in adj[rtadj[p2][0]]:
                    rtadj[p2] += [rtadj[p1][0]]
                    freeNodes += [adj[rtadj[p1][0]][1]]
                    pendants.pop(p2ind)
                elif adj[rtadj[p1][0]][1] in adj[rtadj[p2][0]]:
                    rtadj[p2] += [rtadj[p1][0]]
                    freeNodes += [adj[rtadj[p1][0]][0]]
                    pendants.pop(p2ind)


    groups = fs.findSets(rtadj,n)

    if len(groups.groups()) > 1:

        for g in groups.groups():
            if len(g) == 1:
                connectSing2Group(adj,rtadj,g,freeNodes,n)
        groups = fs.findSets(rtadj,n)
        pendants = [index for index,i in enumerate(rtadj) if len(i) == 1]
    
        if len(groups.groups()) > 1:
            connectDisjoint(adj,rtadj,groups.groups(),freeNodes,n)
        
    return groups.groups(),rtadj

def connectSing2Group(adj,rtadj,single,freeNodes,n=10):
    pendant = rtadj[single[0]][0]
    connectors = []
    for rindex,r in enumerate(rtadj):
        if rindex != single[0]:
            for i in r:
                if adj[pendant][0] in adj[i]:
                    if r in connectors:
                        breakcycle = r.pop(1)
                        r += [pendant]
                        freeNodes += [adj[pendant][1]]
                        
                    else:
                        connectors += [r]
                elif adj[pendant][1] in adj[i]:
                    if r in connectors:
                        breakcycle = r.pop(1)
                        r += [pendant]
                        freeNodes += [adj[pendant][0]]
                    else:
                        connectors += [r]

    for i in rtadj:
        if breakcycle in i:
            i.remove(breakcycle)
            freeNodes += adj[i[0]]
            

    
    print(freeNodes)

def connectDisjoint(adj, rtadj,groups,freeNodes,n=10):
    pendants = [index for index,i in enumerate(rtadj) if len(i) == 1]
    pDiffGroups = [0]*len(pendants)

    for gindex,i in enumerate(groups):
        for pindex, j in enumerate(pendants):
            if j in i:
                pDiffGroups[pindex] += gindex

    print(pDiffGroups)

    

    

    


if __name__ == '__main__':
    adj = [[0, 8], [1, 5], [2, 0], [3, 0], [4, 6], [5, 9], [6, 3], [7, 3], [8, 2], [9, 6], [0, 2], [1, 5], [2, 8], [3, 9], [4, 8], [5, 4], [6, 7], [7, 9], [8, 2], [9, 7]]
    rtadj = [[10], [11], [12], [13], [14, 15], [15], [9, 16], [16, 19], [12, 14], [9, 19], [], [], [], [], [], [], [], [], [], []]

    g,rtadj = connectSingles(adj,rtadj)
    #rtadj = connectGroups(adj,rtadj,g)

    
    '''
    adj:  [[0, 8], [1, 5], [2, 0], [3, 0], [4, 6], [5, 9], [6, 3], [7, 3], [8, 2], [9, 6], [0, 2], [1, 5], [2, 8], [3, 9], [4, 8], [5, 4], [6, 7], [7, 9], [8, 2], [9, 7]]
    rtadj:  [[10], [11], [12], [13], [14, 15], [15], [9, 16], [16, 19], [12, 14], [9, 19], [], [], [], [], [], [], [], [], [], []]
    '''
