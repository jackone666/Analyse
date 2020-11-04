import matplotlib
from sklearn.cluster import AffinityPropagation
import pandas as pd

from ReadExpertmap.readexpertmap import readExpertMap

matplotlib.use('TkAgg')  # 大小写无所谓 tkaGg ,TkAgg 都行
from models.quotaIndividual.quotaIn import quota
import numpy as np
import plotly.graph_objects as go
import xlrd
import xlwt
from notebooks import readToChapterJson

book = xlwt.Workbook(encoding="utf-8")  # 创建工作簿
sheet = book.add_sheet("sheet")  # 创建工作表格
dataXlsx = xlrd.open_workbook('../data/z-scoreResult/score.xlsx'
                              '')
table = dataXlsx.sheet_by_name("Sheet1")
rowsNum = table.nrows
colsNum = table.ncols

quotaDic = {}
highScore = []
lowScore = []
charptIndex = []

nameTotal = []
for i in range(4, 15):
    chapter = "c" + i.__str__()
    chapterJson, name = readToChapterJson.readToChapterJson(chapter)
    for j in chapterJson.keys():
        if str(chapterJson.get(j)).__contains__("root"):
            nameTotal.append(name[int(j) - 1])
            dataTemp = np.array(quota(readExpertMap(i - 4)))  # 零值替换
            dataTemp[dataTemp == 0] = 1
            quotaDic[chapter + j] = list(np.divide(np.array(quota(chapterJson.get(j))), dataTemp))
            print(chapter + "________" + j)
            highScore.append(table.cell(int(j), (i - 2) * 2).value)
            lowScore.append(table.cell(int(j), (i - 2) * 2 + 1).value)
            charptIndex.append(i - 1)
print(quotaDic)
# fig, ax = plt.subplots(1,3,figsize=(15, 5))
#
# for idx, neighbor in enumerate([2, 20, 100,200,300,400,500]):
#     isomap = Isomap( n_components=2, n_neighbors=neighbor)
#     new_X_isomap = isomap.fit_transform(list(quotaDic.values()))
#
#     ax[idx].scatter(new_X_isomap[:,0], new_X_isomap[:,1])
#     ax[idx].set_title("Isomap (n_neighbors=%d)"%neighbor)
#
# plt.show()
# kmeans
# y_pred = KMeans(n_clusters=3,random_state=9).fit_predict(list(quotaDic.values()))
# print("----------------------------")
# for i in range(list(y_pred).__len__()):
#     print(str(list(quotaDic.keys())[i])+"____"+str(list(y_pred)[i]))
# AP
af = AffinityPropagation(preference=-50).fit(list(quotaDic.values()))
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_
# print(list(quotaDic.values()))
# print(list(quotaDic.keys()))
n_clusters_ = len(cluster_centers_indices)
print(n_clusters_)
print(labels)
# mds = MDS(n_components=3)   #多维缩放
# mds.fit(list(quotaDic.values()))
# a = mds.embedding_
# print(a)
# 三维坐标创建
# fig=plt.figure()
# ax1 = Axes3D(fig)
# ax1.scatter3D(np.array(a[:,0]),np.array(a[:,1]),np.array(a[:,2]),c=labels)  #绘制散点图
# plt.show()
# 平行坐标展示
# 建立pd数组
cols = ['color', '节点个数', '纵向连接个数', '总宽度', '路径总条数', '网路直径']
index = list(quotaDic.keys())
npStructData = np.column_stack((labels, list(quotaDic.values())))
pdStructData = pd.DataFrame(npStructData, columns=cols, index=index)  # pd结构矩阵构造完成
# print(pdStructData)
scaleAxis = {}  # 纵坐标范围
for i in range(1, cols.__len__()):
    maxMin = [min(npStructData[:, i]), max(npStructData[:, i])]
    scaleAxis[cols[i]] = maxMin
# print(scaleAxis)
dimensions = []
for i in scaleAxis.keys():
    dicTemp = {'range': scaleAxis.get(i), 'label': i, 'values': pdStructData[i].values}
    dimensions.append(dicTemp)
# print(dimensions)
fig = go.Figure(data=go.Parcoords(
    line=dict(color=pdStructData['color'],
              colorscale=[[0, 'green'], [0.5, 'red'], [1.0, 'blue']]),
    dimensions=dimensions))

fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white'
)
fig.show()
# print(a)
# plt.scatter(a[:, 0], a[:, 1], c=labels)
# plt.show()
# print("-------------")

# quotaStu = np.array(quotaDic.keys())
# cluResult = np.array(labels)
# tansResult = np.transpose(cluResult)  # 分类矩阵转置
# print(tansResult)
# print(quotaDic.keys())
# cluToEx=pd.DataFrame(tansResult, index=list(quotaDic.keys()))
# cluToEx.to_excel("分类.xlsx")
