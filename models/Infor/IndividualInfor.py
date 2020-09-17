import math
import sys

count = 0
sys.setrecursionlimit(100000000)


def nodeInformationentropy(node: str, tree):
    rowSumDic = {}  # 以字典储存每个节点出度
    listTemp = list(tree.index)
    rowSum = list(tree.sum(axis=1))  # 每个节点出度和  列表
    for i in range(0, rowSum.__len__()):
        rowSumDic[listTemp[i]] = rowSum[i]

    # print(rowSumDic.keys().__len__())
    def nodeCount(nodeTemp: str):  # 获取树的所有子树节点
        global count
        if rowSumDic.get(nodeTemp) == 0:
            return
        for j in rowSumDic.keys():
            if tree.at[nodeTemp, j] == 1:
                count = count + 1
                nodeCount(j)
                return

    global count
    count = 0
    nodeCount(node)
    nodeChildNum = count  # 节点node所有子结点个数
    result = 0
    if rowSumDic.get(node) == 0:  # 叶子节点信息熵为0
        return 0
    for j in tree.index:
        if tree.at[node, j] == 1:
            count = 0
            nodeCount(j)
            result = result - (count + 1) / nodeChildNum * math.log((count + 1) / nodeChildNum, len(rowSumDic) - 1)
    return result
