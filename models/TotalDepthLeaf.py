def totalDepthLeaf(tree, level):
    rowSumDic = {}  # 以字典储存每个节点出度
    listTemp = list(tree.index)
    rowSum = list(tree.sum(axis=1))  # 每个节点出度和  列表
    for i in range(0, rowSum.__len__()):
        rowSumDic[listTemp[i]] = rowSum[i]
        totalDepth = 0
    for i in rowSumDic.keys():
        if rowSumDic.get(i) == 0:  # 如果为叶子节点
            for k in range(0, len(level)):
                if level[k].__contains__(i):
                    totalDepth = totalDepth + k
    return totalDepth
