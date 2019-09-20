#connect disjoint sets
import numpy as np
import unionfind as uf
import findsets as fs
from itertools import chain

'''
The following are the problematic cases i've found and need to address, and how i've addressed them (plan to):
1)P - sets are disjoint, but both are acyclic, or isolated singleton:
	S - compare singletons by their degree 1 nodes, if you find a pair between disjoint sets: connect.
2)P - sets are disjoint, one is cyclic, one is not, or isolated singleton:
	S - compare cyclic set to singletons in disjoint set, find connector, connect, and delete excess node.
3)P - disjoint sets, and all cyclic:
	S - compare nodes in one set to others, find connector, connect, and delete excess node.
4)P - sets are disjoint, acyclical, and connectors 'miss':
	S - compare singletons in same sets, create cycle, then perform solution (3), or (2).
	
Given that 4 encompasses solutions 3 and 2, i figure we start there.
create an alg that makes a cycle, then finds a connector.
We can do that after we attempt solution 1.
'''



adj = [[0, 8], [1, 5], [2, 0], [3, 0], [4, 6], [5, 9], [6, 3], [7, 3], [8, 2], [9, 6], [0, 2], [1, 5], [2, 8], [3, 9], [4, 8], [5, 4], [6, 7], [7, 9], [8, 2], [9, 7]]
rtadj = [[10], [11], [12], [13], [14, 15], [15], [9, 16], [16, 19], [12, 14], [9, 19], [], [], [], [], [], [], [], [], [], []]
n = 10

#Step one: find pendants
singletons = [ r[0] for r in rtadj if len(r) == 1]

#Step two: find disjoint sets, store their rtadj values
sets = fs.findSets(rtadj,n)
groups = [[]for i in range(len(sets.groups()))]

for i in range(len(groups)):
    group = []
    for r in sets.groups()[i]:
        group += rtadj[r]
    groups[i] += group

#step three: find freenodes:

freeNodesdict = {s:adj[s] for g in groups for s in singletons if len(g) == 1 and s in g}
singletons = [i for i in singletons if i not in freeNodesdict.keys()]

freeNodesdict.update({s:adj[s][0] for g in groups for s in singletons for n in g if (adj[s][1] in adj[n]) and \
                   (adj[s][1] not in freeNodesdict.values()) and len(g) > 1})
freeNodesdict.update({s:adj[s][1] for g in groups for s in singletons for n in g if (adj[s][0] in adj[n]) and \
                   (adj[s][0] not in freeNodesdict.values()) and len(g) > 1})
 
#step four: connect pendants.
print(rtadj)

for p in freeNodesdict:
    if not isinstance(p,list):
        for p2 in freeNodesdict:
            if isinstance(freeNodesdict[p2],list):
                if freeNodesdict[p] in freeNodesdict[p2] and p != p2:
                    print('hello')
                    rtadj[p] += [rtadj[p2]]

print(rtadj)



















    

