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
for i in range(3, 15):
    chapter = "c" + i.__str__()
    chapterJson, name = readToChapterJson.readToChapterJson(chapter)
    for j in chapterJson.keys():
        if str(chapterJson.get(j)).__contains__("root"):
            nameTotal.append(name[int(j) - 1])
            quotaDic[chapter + j] = quota(chapterJson.get(j))
            print(chapter + "________" + j)
            highScore.append(table.cell(int(j), (i - 2) * 2).value)
            lowScore.append(table.cell(int(j), (i - 2) * 2 + 1).value)
            charptIndex.append(i - 1)
print(quotaDic)

af = AffinityPropagation(preference=-50).fit(list(quotaDic.values()))
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_
# print(list(quotaDic.values()))
# print(list(quotaDic.keys()))
n_clusters_ = len(cluster_centers_indices)
print(n_clusters_)
print(labels)
cols = ['color', '平均宽度', '平均叶子深度', '平均路径深度','pr均值','D','R']

index = list(quotaDic.keys())
npStructData = np.column_stack((labels, list(quotaDic.values())))
pdStructData = pd.DataFrame(npStructData, columns=cols, index=index)  # pd结构矩阵构造完成

# 构造输出矩阵
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
# fig.show()
# 给np矩阵扩充列
CluIndex = ['姓名', 'highScore', 'lowScore', '类别', '平均宽度', '平均叶子深度', '平均路径深度','pr均值','D','R']
merge1 = np.column_stack((lowScore, npStructData))
merge2 = np.column_stack((highScore, merge1))
merge3 = np.column_stack((nameTotal, merge2))
pd.DataFrame(merge3, index=charptIndex, columns=CluIndex).to_excel("CluResult.xlsx")
