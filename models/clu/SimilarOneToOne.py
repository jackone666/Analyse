import grakel
from grakel import Graph


def similarOneToOne(map_1, map_2):
    map_1_array = map_1.values
    map_2_array = map_2.values
    # print(map_2_array)
    # for i in range(0, map_1_array.__len__()):
    #     for j in range(0, map_1_array.__len__()):
    #         if map_1_array[i][j] == 'nan':
    #             map_1_array[i][j] = 0
    # for i in range(0, map_2_array.__len__()):
    #     for j in range(0, map_2_array.__len__()):
    #         if map_2_array[i][j] == 'nan':
    #             map_2_array[i][j] = 0

    # print(map_2_array)
    # print(map_1_array)
    map_1_node_labels = {}
    map_2_node_labels = {}
    for i in range(0, map_1.index.__len__()):  # 图节点标签构造
        map_1_node_labels[i] = str(map_1.index[i])
        map_1_node_labels[i] = str(map_1.index[i])
    for i in range(0, map_2.index.__len__()):  # 图节点标签构造
        map_2_node_labels[i] = str(map_2.index[i])
    H1 = Graph(initialization_object=map_1_array, node_labels=map_1_node_labels)
    H2 = Graph(initialization_object=map_2_array, node_labels=map_2_node_labels)
    sp_kernel = grakel.ShortestPath(normalize=True)
    sp_kernel.fit_transform([H1])
    print(map_1)
    return sp_kernel.transform([H2])
