import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import AffinityPropagation
import pandas as pd

matplotlib.use('TkAgg')  # 大小写无所谓 tkaGg ,TkAgg 都行
import matplotlib.pyplot as plt
from models.clu.readToChapterJson import readToChapterJson
from models.quotaIndividual.quotaIn import quota
from sklearn.manifold import Isomap  # 降维
from sklearn.cluster import KMeans
import numpy as np
from sklearn.manifold import MDS
import plotly.graph_objects as go

quotaDic = {}
for i in range(4, 16):
    chapter = "c" + i.__str__()
    chapterJson = readToChapterJson(chapter)
    for j in chapterJson.keys():
        if str(chapterJson.get(j)).__contains__("root"):
            quotaDic[chapter + j] = quota(chapterJson.get(j))
            print(chapter + "________" + j)

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
cols = ['color', '平均宽度', '平均叶子深度', '平均路径深度', 'pr均值','D','R']
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
              colorscale=[[0, 'green'], [0.5, 'red'], [1.0, 'rgb(0, 0, 255)']]),
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
