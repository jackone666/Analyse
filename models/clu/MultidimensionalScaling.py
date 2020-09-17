from sklearn.manifold import MDS
import matplotlib.pyplot as plt


def MulScaling(matriIndex):
    mds = MDS()
    mds.fit(matriIndex.values)
    a = mds.embedding_
    return a, matriIndex.index
