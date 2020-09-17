import networkx as nx


def gStruct(map):
    G = nx.DiGraph()
    for i in list(map.index):
        for j in list(map.index):
            if map.loc[i][j] == 1:
                G.add_edge(i, j, weight=1)
    return G
