from sklearn import metrics

from sklearn.cluster import KMeans, spectral_clustering, SpectralClustering
from models.clu.SimilarMatri import similarMatri
from models.clu.MultidimensionalScaling import MulScaling
import matplotlib.pyplot as plt
import matplotlib
import pandas as np
from sklearn.cluster import DBSCAN
from models.drawMap.Tomap import toMap

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签)

similarMat = similarMatri(col="c15")
distanceMat = 1 - similarMat
# print(distanceMat)
coordinateSystemMatrix, index = MulScaling(distanceMat)
# print(coordinateSystemMatrix)
# k_means

print(coordinateSystemMatrix)
y_pred = KMeans(n_clusters=4, random_state=9).fit_predict(coordinateSystemMatrix)
print("----------------------------")
print(y_pred)
toMap("c15", y_pred)
plt.scatter(coordinateSystemMatrix[:, 0], coordinateSystemMatrix[:, 1], c=y_pred)
for i in range(len(coordinateSystemMatrix)):
    plt.annotate(index[i], xy=(coordinateSystemMatrix[i][0], coordinateSystemMatrix[i][1]),
                 xytext=(coordinateSystemMatrix[i][0] + 0.1, coordinateSystemMatrix[i][1] + 0.1))
plt.show()

# dbscan

# y_pred = DBSCAN().fit_predict(coordinateSystemMatrix)
# print(y_pred)
# makerS = []
# plt.scatter(coordinateSystemMatrix[:, 0], coordinateSystemMatrix[:, 1], c=y_pred, s=50)
# for i in range(len(coordinateSystemMatrix)):
#     plt.annotate(index[i], xy=(coordinateSystemMatrix[i][0], coordinateSystemMatrix[i][1]),
#                  xytext=(coordinateSystemMatrix[i][0] + 0.1, coordinateSystemMatrix[i][1] + 0.1))
#
# plt.show()
# 普分类  有点问题
# for index, gamma in enumerate((0.01,0.1,1,10)):
#     for index, k in enumerate((3,4,5,6)):
#         y_pred = SpectralClustering(n_clusters=k, gamma=gamma).fit_predict(similarMat)
#         print("Calinski-Harabasz Score with gamma=", gamma, "n_clusters=", k,"score:", metrics.calinski_harabaz_score(similarMat, y_pred))
# sc = SpectralClustering(3, affinity='precomputed', n_init=10, assign_labels='discretize')
# y_pred = sc.fit_predict(similarMat)
# plt.scatter(coordinateSystemMatrix[:, 0], coordinateSystemMatrix[:, 1], c=y_pred, s=50)
# for i in range(len(coordinateSystemMatrix)):
#     plt.annotate(index[i], xy=(coordinateSystemMatrix[i][0], coordinateSystemMatrix[i][1]),
#                  xytext=(coordinateSystemMatrix[i][0] + 0.1, coordinateSystemMatrix[i][1] + 0.1))
# print(y_pred)
# plt.show()
