import matplotlib
from sklearn.cluster import AffinityPropagation
import pandas as pd

matplotlib.use('TkAgg')  # 大小写无所谓 tkaGg ,TkAgg 都行
from models.quotaIndividual.quotaIn import quota
import numpy as np
import plotly.graph_objects as go
import xlrd
import xlwt
from notebooks import readToChapterJson

book = xlwt.Workbook(encoding="utf-8")  # 创建工作簿
sheet = book.add_sheet("sheet")  # 创建工作表格
dataXlsx = xlrd.open_workbook('../data/z-scoreResult/z-Score.xlsx')
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
cols = ['color', '1节点个数', '2叶子节点个数', '3第二层节点数貌似论文称为分支个数', '4 最大层宽度',
        '5 纵向连接个数即等级关系的个数', '6横向连接个数即交叉关系的个数', '7总宽度  树结构每一层的宽度和',
        '8平均宽度，总宽度除以树结构的总结点', ' 9层数', '10最大叶节点深度', '11叶节点深度总和',
        '12根节点到叶节点的路径总条数', '13平均叶子深度', '14路径总深度', '15路径总条数',
        '16平均路径深度(16/17)', '17Hub均值--H', '18Authority均值-A',
        '19 pr均值', '20 知识存储容量S=H/A', '21网络直径T', '22知识分布性D=log(T*H(1-A)', '23知识检索R=√(S*P)']
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
CluIndex = ['姓名', 'highScore', 'lowScore', '类别', '1节点个数', '2叶子节点个数', '3第二层节点数貌似论文称为分支个数', '4 最大层宽度',
            '5 纵向连接个数即等级关系的个数', '6横向连接个数即交叉关系的个数', '7总宽度  树结构每一层的宽度和',
            '8平均宽度，总宽度除以树结构的总结点', ' 9层数', '10最大叶节点深度', '11叶节点深度总和',
            '12根节点到叶节点的路径总条数', '13平均叶子深度', '14路径总深度', '15路径总条数',
            '16平均路径深度(16/17)', '17Hub均值--H', '18Authority均值-A',
            '19 pr均值', '20 知识存储容量S=H/A', '21网络直径T', '22知识分布性D=log(T*H(1-A)', '23知识检索R=√(S*P)']
merge1 = np.column_stack((lowScore, npStructData))
merge2 = np.column_stack((highScore, merge1))
merge3 = np.column_stack((nameTotal, merge2))
pd.DataFrame(merge3, index=charptIndex, columns=CluIndex).to_excel("CluResult.xlsx")
