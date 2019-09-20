import numpy as np
import generateAdjacency as gA
from connectsets import connectSets
import matplotlib.pyplot as plt
import networkx as nx

#find a hamiltonian path in a graph,
# code taken from:
#https://stackoverflow.com/questions/47982604/hamiltonian-path-using-python

'''
def hamilton(G, size, pt, path=[]):
    print('hamilton called with pt={}, path={}'.format(pt, path))
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
        print('path {} is a dead end'.format(path))
    else:
        print('pt {} already in path {}'.format(pt, path))
'''
n = 10
def trial():

    adj = gA.GenerateAdj(n = 10)
    #print('adj: ',adj)

    tadj = gA.transAdjacency(adj)
    #print('tadj: ',tadj)
    rtadj = gA.reduceTransAdj(tadj)
    #print('rtadj: ',rtadj)
    start = 0
    for i in rtadj:
        if len(i) == 1:
            start = i[0]

    deg = gA.getDegrees(rtadj, n = 10)
    odd = 0
    for i in deg:
        if i == 4:
            #print('not connected')
            return 0,0,0,0,deg
        elif (i%2) != 0:
            odd += 1
            if odd > 2:
                #print('no euler walk')
                return 0,0,0,0,deg


    return 1, adj,tadj,rtadj, deg


for i in range(1000):
    #print(i)
    ret, adj,tadj,rtadj, deg = trial()
    #ret, adj, deg = trial()
    if ret == 1:
        print(i)
        break

with open('c:/Users/RandyCocks/Desktop/AndysStuff/Graphs.txt','a') as graphs:
    graphs.write("Adj: "+ str(adj) + '\n')
    graphs.write("Tadj: " + str(tadj) + '\n')
    graphs.write("Rtadj: " + str(rtadj) + '\n')
    graphs.write("degrees: " + str(deg) + '\n\n')

G = nx.Graph()
RG = nx.Graph()
G.add_nodes_from([0,9])
RG.add_nodes_from([0,9])

for i in adj:
    G.add_edge(i[0],i[1])

for i in range(n):
    RG.add_edge(rtadj[i][0],rtadj[i][1])



plt.subplot(121)
nx.draw(G,with_labels=True,node_size=20)

plt.subplot(122)
nx.draw(RG,with_labels=True,node_size=20)


plt.show()
    
print('adj: ',adj)
print('rtadj: ',rtadj)
#newrtadj = connectSets(adj,rtadj)
#print('new rtadj :', newrtadj)
#print('tadj: ',tadj)
#print('rtadj: ', rtadj)
print(deg)

#hamilton(adj,len(adj),1,path = [])


    








    
