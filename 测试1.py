import xlrd
from models import ParseToMatrix
dataXlsx = xlrd.open_workbook('data/cbj-导图处理结束.xlsx')
table = dataXlsx.sheet_by_name("Sheet1")
rowsNum = table.nrows
ConceptMapQuota = []
colsStudentName = []  # 存储名字
rowsQuotaName = ['1节点个数', '2叶子节点个数', '3第二层节点数貌似论文称为分支个数', '4 最大层宽度',
                 '5 纵向连接个数即等级关系的个数', '6横向连接个数即交叉关系的个数', '7总宽度  树结构每一层的宽度和',
                 '8平均宽度，总宽度除以树结构的总结点', '9信息熵总和', '10 非叶子节点平均信息熵', ' 11层数', '12最大叶节点深度',
                 '13叶节点深度总和', '14 根节点到叶节点的路径总条数  等于叶节点个数', '15平均叶子深度', '16路径总深度  即每个节点深度和',
                 '17路径总条数     根到所有节点路径个数和', '18平均路径深度(16/17)', '19Hub均值--H', '20Authority均值-A',
                 '21 pr均值', '22 知识存储容量S=H/A', '23网络直径T', '24知识分布性D=log(T*H(1-A)', '25知识检索R=√(S*P)']  # 存储指标名字
for j in range(0, 19):
    for i in range(1, rowsNum):
        colData = table.cell(i, j).value
        if str(colData).__contains__("root"):
            colsStudentName.append(table.cell(i, 1).value)
            tree, level, map = ParseToMatrix.returnMatrix(colData)
            print(str(table.cell(i, 0).value)+"----"+str(table.cell(0, j).value))