def pathRootToNodeTotal(level):
    pathTotal = 0  # 16路径总深度（根到所有节点路径长度和）
    for i in range(0, level.__len__()):  # 每一层的节点数*节点所在层数
        pathTotal = pathTotal + i * len(level[i])
    return pathTotal
