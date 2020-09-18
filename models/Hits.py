import networkx as nx
from models.GS.GStruct import gStruct


def hits(map):
    G = gStruct(map)
    hitsResult = nx.hits(G, max_iter=100000)
    totalH = 0
    totalA = 0
    for i in hitsResult[0].keys():
        totalH = totalH + hitsResult[0].get(i)
        totalA = totalA + hitsResult[1].get(i)
    return totalH / hitsResult[0].__len__(), totalA / hitsResult[0].__len__(),
