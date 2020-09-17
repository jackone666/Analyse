# from pandas import np
import math
import demjson
import networkx as nx
import numpy as np
import pandas as pd
from graphviz import Digraph


def returnMatrix(jsonStr):
    jsonObject = demjson.decode(jsonStr)
    # print(jsonObject)
    # print(jsonObject["root"]["text"])
    treeData = jsonObject['root']  # 树节点  不包含例子和横向节点
    summariesData = jsonObject['summaries']
    summariesIdNode = {}  # 储存sunmary
    for i in summariesData:
        summariesIdNode[i['trees'][0]] = i['text']
    linksData = jsonObject['links']  # 横向链接
    linksIdNode = {}  # 储存links 其中两个id 以&分割
    for i in linksData:
        # print(i)
        inAndOut = i['input'] + '&' + i['output']
        linksIdNode[inAndOut] = i['text']
    # print(linksIdNode)
    idNodeDic = {}  # 储存id和节点的对应关系
    idTemp = []  # 储存变量的临时ID，存到字典
    listTree = []  # 储存节点层数和文本
    nodeLevelNum = 0  # 储存不包含sunmmay的层数
    for i in dict_generator(treeData):
        # print(i)
        if i.__contains__('text') and not i.__contains__('connectText'):
            listTree.append(i)
            if i.__len__() - 1 > nodeLevelNum:
                nodeLevelNum = i.__len__() - 1
        if i.__contains__('id'):
            idTemp.append(i[-1])
    for i in range(0, idTemp.__len__()):
        idNodeDic[idTemp[i]] = listTree[i][-1]
    # print(idNodeDic)  # 储存了id和node的对应关系
    # print('.'.join(i[0:-1]), ':', i[-1])
    # print(listTree)
    indexText = []  # 储存树的索引  不包括summary节点
    for i in listTree:
        indexText.append(i[-1])
    nodes = list(set(list(indexText + list(summariesIdNode.values()))))  # 节点个数和重复节点处理
    mapMatrix = np.zeros((nodes.__len__(), nodes.__len__()))  # 建立全部节点矩阵
    mapMatrixIndex = pd.DataFrame(mapMatrix, index=nodes, columns=nodes)  # 建立所有节点矩阵，以节点内容为索引

    for i in range(0, listTree.__len__() - 1):  # 纵向节点关系存入
        if len(listTree[i]) < len(listTree[i + 1]):
            mapMatrixIndex.at[listTree[i][-1], listTree[i + 1][-1]] = 1
            indexNode = listTree[i][-1]
        if len(listTree[i]) == len(listTree[i + 1]):
            mapMatrixIndex.at[[indexNode], listTree[i + 1][-1]] = 1
            # print(indexNode+'--------'+listTree[i + 1][-1])
        if len(listTree[i + 1]) == 3:  # 第一层节点数
            mapMatrixIndex.at[listTree[0][-1], listTree[i + 1][-1]] = 1
        if len(listTree[i]) > len(listTree[i + 1]):
            j = i
            while 1:
                if listTree[j].__len__() == listTree[i + 1].__len__() - 1 or listTree[j].__len__() == 2:
                    break
                j = j - 1
            mapMatrixIndex.at[listTree[j][-1], listTree[i + 1][-1]] = 1
            indexNode = listTree[j][-1]

    for i in summariesIdNode.keys():
        mapMatrixIndex.at[idNodeDic.get(i), summariesIdNode.get(i)] = 1  # 纵向节点关系存储结束  返回1：树结构矩阵mapMatrixIndex

    nodeSummaryLevel = []  # 储存层次关系  每个节点的层次  每个层数的节点
    for i in range(0, nodeLevelNum):
        nodeSummaryLevel.append([])  # 构造储存结构
    # print(listTree)
    for i in listTree:
        nodeSummaryLevel[i.__len__() - 2].append(i[-1])
    levelTemp = []  # 储存summary扩展的节点
    for i in summariesIdNode.values():
        for j in nodes:  # 遍历找到summary节点链接的普通节点
            if mapMatrixIndex.at[j, i] == 1:
                for k in range(0, len(nodeSummaryLevel)):
                    if nodeSummaryLevel[k].__contains__(j) and k < len(nodeSummaryLevel) - 1:
                        nodeSummaryLevel[k + 1].append(i)  # 如果上一层包含  则下一层增加例子
                    if nodeSummaryLevel[k].__contains__(j) and k == len(nodeSummaryLevel) - 1:
                        levelTemp.append(i)
    if levelTemp.__len__() != 0:
        nodeSummaryLevel.append(levelTemp)  # 层次关系  返回2：nodeSummaryLevel
    # print(nodeSummaryLevel)
    # print(nodeSummaryLevel)
    # print(nodeLevelNum)  #层数波包括summary
    ###########################横向链接矩阵构造
    nodeLinksSummaryMatrix = np.zeros(
        (list(set(list(nodes + list(linksIdNode.values())))).__len__(), list(set(list(nodes + list(linksIdNode.values())))).__len__()))
    nodeLinksSummaryMatrixIndex = pd.DataFrame(nodeLinksSummaryMatrix,
                                               index=list(set(list(nodes + list(linksIdNode.values())))),columns=list(set(list(nodes + list(linksIdNode.values())))))
    for i in nodes:  # 将原有的不包括横向连接的复制进来
        for j in nodes:
            nodeLinksSummaryMatrixIndex.at[i, j] = mapMatrixIndex.loc[i][j]
    for i in linksIdNode.keys():  # 将横向链接情况输入
        inputAndOutSplit = i.split('&')
        nodeLinksSummaryMatrixIndex.at[idNodeDic.get(inputAndOutSplit[0]), linksIdNode.get(i)] = 1  # 横向连接的输入节点
        nodeLinksSummaryMatrixIndex.at[linksIdNode.get(i), idNodeDic.get(inputAndOutSplit[1])] = 1  # 横向连接的输出节点
    # 返回3：横向链接矩阵  nodeLinksSummaryMatrixIndex
    return mapMatrixIndex.fillna(0), nodeSummaryLevel, nodeLinksSummaryMatrixIndex.fillna(0)


def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        for key, value in indict.items():
            if isinstance(value, dict):
                if len(value) == 0:
                    yield pre + [key, '{}']
                else:
                    for d in dict_generator(value, pre + [key]):
                        yield d
            elif isinstance(value, list):
                if len(value) == 0:
                    yield pre + [key, '[]']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            elif isinstance(value, tuple):
                if len(value) == 0:
                    yield pre + [key, '()']
                else:
                    for v in value:
                        for d in dict_generator(v, pre + [key]):
                            yield d
            else:
                yield pre + [key, value]
    else:
        yield indict


# if __name__ == '__main__':
#     returnMatrix()
