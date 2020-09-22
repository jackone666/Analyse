import numpy as np
import pandas as pd


def z_scoreCu(col):
    temp = []
    npData = np.array(col)
    # print(npData)
    aver = np.average(npData)
    sTd = np.std(npData)
    # print(aver)
    # print(sTd)
    for i in npData:
        temp.append((i - aver) / sTd)
    return temp


matrixResult = []
for i in range(1, 25):
    matrix = pd.read_excel("../data/学生分数.xlsx")
    colsResult = z_scoreCu(matrix[i])
    # print(colsResult)
    matrixResult.append(colsResult)
resultMatri = np.transpose(matrixResult)
pd.DataFrame(resultMatri).to_excel("../data/z-scoreResult/z-score.xlsx")
