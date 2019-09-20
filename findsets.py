# create sets:

import unionfind as uf


def findSets(rtadj,n):

    groups = uf.unionfind(n)

    for i in range(len(rtadj)):
        if len(rtadj[i]) == 1:
            for j,edge in enumerate(rtadj):
                if rtadj[i] in edge:
                    groups.unite(i,j)
        elif len(rtadj[i]) == 2:
            for j,edge in enumerate(rtadj):
                if rtadj[i][0] in edge or rtadj[i][1] in edge:
                    groups.unite(i,j)

    return groups
