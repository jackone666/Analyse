import networkx as nx
from models.GS.GStruct import gStruct


def pageRank(map):
    total = 0
    G = gStruct(map)
    result = nx.pagerank(G, max_iter=100000)
    for i in result.keys():
        total = total + result.get(i)
    return total / result.__len__()
