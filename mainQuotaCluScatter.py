

# 暂停项目

import plotly.offline as pltoff   #离线模式
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
mpl.rcParams['font.sans-serif'] = ['SimHei']   #画图中文乱码
mpl.rcParams['font.serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
quotaDic = {}
charptIndex = []
nameTotal = []
charptTotal = []
for i in range(1, 2):
    nameArray=[]
    chapter = "c" + i.__str__()
    chapterJson, name = readToChapterJson.readToChapterJson(chapter)
    for j in chapterJson.keys():
        if str(chapterJson.get(j)).__contains__("root"):
            nameArray.append(name[int(j) - 1])     #名字存储
            dataTemp = np.array(quota(readExpertMap(i - 4)))  # 零值替换
            dataTemp[dataTemp == 0] = 1
            quotaDic[chapter + j] = list(np.divide(np.array(quota(chapterJson.get(j))), dataTemp))
            print(chapter + "________" + j)
            charptIndex.append(i - 1)
    charptTotal=charptTotal+[i-1]*nameArray.__len__()
    nameTotal=nameTotal+nameArray
print(quotaDic.keys().__len__())
print(nameTotal.__len__())
print(charptTotal.__len__())
af = AffinityPropagation(preference=-50).fit(list(quotaDic.values()))
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_
n_clusters_ = len(cluster_centers_indices)
print(n_clusters_)
print(type(labels))
# plt.scatter(charptTotal,nameTotal,c=labels)
# plt.show()
fig = go.Figure(data=go.Scatter(x=charptTotal, y=nameTotal, mode="markers",marker=dict(color=labels+1)))
pltoff.plot(fig, filename="可视化.html")
fig.show()
