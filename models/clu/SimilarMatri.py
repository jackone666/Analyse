from models.clu.ReadToChapterMatri import readToChapterMaTri
from models.clu.SimilarOneToOne import similarOneToOne
import numpy as np
import pandas as pd


def similarMatri(col):
    mapDic = readToChapterMaTri(col)
    mapMatrix = np.zeros((mapDic.keys().__len__(), mapDic.keys().__len__()))
    mapMatrixIndex = pd.DataFrame(mapMatrix, index=mapDic.keys(), columns=mapDic.keys())
    # print(mapDic)
    for i in mapDic.keys():
        for j in mapDic.keys():
            oneToneSimilar = similarOneToOne(mapDic.get(i), mapDic.get(j))
            mapMatrixIndex.at[i, j] = oneToneSimilar[0][0]
            print(i)
    return mapMatrixIndex
