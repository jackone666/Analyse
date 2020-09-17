def leadNodeNum(tree):
    rowSum = list(tree.sum(axis=1))  # 每个节点出度和  列表
    # print(rowSum)
    leafNodeNum = rowSum.count(0)
    return leafNodeNum
