import networkx as nx
from models.GS.GStruct import gStruct


def netDiameter(map):
    G = gStruct(map)
    diameter = 0  # 22网络直径-T
    fordPath = dict(nx.all_pairs_bellman_ford_path_length(G))
    # print(fordPath)
    for i in fordPath.keys():
        for j in fordPath[i]:
            if diameter < fordPath[i][j]:
                diameter = fordPath[i][j]
    return diameter
