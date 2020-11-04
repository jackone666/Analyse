import plotly.offline as pltoff  # 离线模式
import matplotlib
from sklearn.cluster import AffinityPropagation
from ReadExpertmap.readexpertmap import readExpertMap

matplotlib.use('TkAgg')  # 大小写无所谓 tkaGg ,TkAgg 都行
from models.quotaIndividual.quotaIn import quota
import numpy as np
from notebooks import readToChapterJson
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.graph_objects as go

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 画图中文乱码
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
quotaDic = {}
charptIndex = []
nameTotal = []
charptTotal = []
for i in range(3, 14):
    nameArray = []
    chapter = "c" + i.__str__()
    chapterJson, name = readToChapterJson.readToChapterJson(chapter)
    for j in chapterJson.keys():
        if str(chapterJson.get(j)).__contains__("root"):
            nameArray.append(name[int(j) - 1])  # 名字存储
            dataTemp = np.array(quota(readExpertMap(i - 4)))  # 零值替换
            dataTemp[dataTemp == 0] = 1
            quotaDic[chapter + j] = list(np.divide(np.array(quota(chapterJson.get(j))), dataTemp))
            print(chapter + "________" + j)
            charptIndex.append(i - 1)
    charptTotal = charptTotal + [i - 1] * nameArray.__len__()
    nameTotal = nameTotal + nameArray
print(quotaDic.keys().__len__())
print(nameTotal.__len__())
print(charptTotal.__len__())
af = AffinityPropagation(preference=-50).fit(list(quotaDic.values()))
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_
n_clusters_ = len(cluster_centers_indices)
print(n_clusters_)
print(labels)
labelsQuota = np.array(labels).reshape(-1, 21).T  # 特征转置    学生聚类
print(labelsQuota)
af = AffinityPropagation(preference=-50).fit(labelsQuota)
cluster_centers_indices = af.cluster_centers_indices_
labelsT = af.labels_
n_clusters_ = len(cluster_centers_indices)
print(n_clusters_)
print(name)
print(labelsT)
nameCluDic = {}
for i in range(0, name.__len__()):
    nameCluDic[name[i]] = labelsT[i]

X1 = []
X2 = []
Y1 = []
Y2 = []
labels1 = []
labels2 = []
for i in range(0, nameTotal.__len__()):
    if nameCluDic.get(nameTotal[i]) == 0:
        X1.append(charptTotal[i])
        Y1.append(nameTotal[i])
        labels1.append(labels[i])
    if nameCluDic.get(nameTotal[i]) == 1:
        X2.append(charptTotal[i])
        Y2.append(nameTotal[i])
        labels2.append(labels[i])
fig1 = go.Figure(data=go.Scatter(x=X1, y=Y1, mode="markers", marker=dict(color=np.array(labels1) + 1)))
pltoff.plot(fig1, filename="可视化1.html")
fig1.show()
fig2 = go.Figure(data=go.Scatter(x=X2, y=Y2, mode="markers", marker=dict(color=np.array(labels2) + 1)))
pltoff.plot(fig2, filename="可视化2.html")
fig2.show()
