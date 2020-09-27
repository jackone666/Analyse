import math

from models import ParseToMatrix, LeafNodeNum, BranchesNum, MaxWith, SumWith, EntropyTotal, NodeLevelNum, \
    TotalDepthLeaf, PathRootToNodeTotal, PathTotalNum, Hits, PageRank, NetDiameter


def quota(data):
    tree, level, map = ParseToMatrix.returnMatrix(data)
    individualQuota = []
    nodeNumber = list(map.index).__len__()  # 1节点个数
    individualQuota.append(nodeNumber)
    leafNodeNum = LeafNodeNum.leadNodeNum(tree)  # 2叶子节点个数
    individualQuota.append(leafNodeNum)
    branchesNum = BranchesNum.branchesNum(level)  # 3第二层节点数  貌似论文称为分支个数
    individualQuota.append(branchesNum)
    maxWith = MaxWith.maxWith(level)  # 4 最大层宽度
    individualQuota.append(maxWith)
    verticalLinksNum = nodeNumber - 1  # 5 纵向连接个数即等级关系的个数
    individualQuota.append(verticalLinksNum)
    transverseLinksNum = list(map.index).__len__() - list(tree.index).__len__()  # 6横向连接个数即交叉关系的个数
    individualQuota.append(transverseLinksNum)
    sumWith = SumWith.sumWith(level)  # 7总宽度  树结构每一层的宽度和
    individualQuota.append(sumWith)
    averageWith = sumWith / list(tree.index).__len__()  # 8平均宽度，总宽度除以树结构的总结点
    individualQuota.append(averageWith)
    # entropyTotal = EntropyTotal.entropyTotal(tree)  # 9信息熵总和
    # individualQuota.append(entropyTotal)
    # notLeafAverEntropy = entropyTotal / (list(tree.index).__len__()) - leafNodeNum  # 10 非叶子节点平均信息熵
    # individualQuota.append(notLeafAverEntropy)
    nodeLevelNum = NodeLevelNum.nodeLevelNum(level)  # 11层数
    individualQuota.append(nodeLevelNum)
    maxDepthLeaf = nodeLevelNum  # 12最大叶节点深度
    individualQuota.append(maxDepthLeaf)
    totalDepthLeaf = TotalDepthLeaf.totalDepthLeaf(tree, level)  # 13叶节点深度总和
    individualQuota.append(totalDepthLeaf)
    rootToLeafNum = leafNodeNum  # 14 根节点到叶节点的路径总条数  等于叶节点个数
    individualQuota.append(rootToLeafNum)
    averLeafDepth = totalDepthLeaf / rootToLeafNum  # 15平均叶子深度
    individualQuota.append(averLeafDepth)
    pathRootToNodeTotal = PathRootToNodeTotal.pathRootToNodeTotal(level)  # 16路径总深度  即每个节点深度和
    individualQuota.append(pathRootToNodeTotal)
    pathTotalNum = PathTotalNum.pathTotalNum(tree)  # 17路径总条数     根到所有节点路径个数和
    individualQuota.append(pathTotalNum)
    averPathDepth = pathRootToNodeTotal / pathTotalNum  # 18平均路径深度(16/17)
    individualQuota.append(averPathDepth)
    hitsHResult, hitsAResult = Hits.hits(map)  # 19Hub均值--H 20Authority均值
    individualQuota.append(hitsHResult)
    individualQuota.append(hitsAResult)
    pageRank = PageRank.pageRank(map)  # 21 pr均值
    individualQuota.append(pageRank)
    knowledgeStorageCapacity = hitsHResult / hitsAResult  # 22 知识存储容量S=H/A
    individualQuota.append(knowledgeStorageCapacity)
    netDiameter = NetDiameter.netDiameter(map)  # 23网络直径T
    individualQuota.append(netDiameter)
    knowledgeDistribution = math.log(netDiameter * hitsHResult * (1 - hitsAResult))  # 24知识分布性D=log(T*H(1-A)
    individualQuota.append(knowledgeDistribution)
    knowledgeSearch = math.sqrt(knowledgeStorageCapacity * pageRank)  # 25知识检索R=√(S*P)
    individualQuota.append(knowledgeSearch)
    return individualQuota
