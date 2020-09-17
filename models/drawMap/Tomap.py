from typing import Any, Union

from graphviz import Digraph  # 画图变量
from models.clu.ReadToChapterMatri import readToChapterMaTri


def toMap(clo, cluArray):
    numClu = 0
    dicMap = readToChapterMaTri(clo)
    for i in dicMap.keys():
        mapMat = dicMap.get(i)
        dot = Digraph(comment='导图', format="pdf",
                      edge_attr={"style": 'dashed', "arrowhead": 'empty', "splines": 'spline'},
                      node_attr={"fontname": "FANGSONG"}, encoding="utf-8")
        for j in mapMat.index:
            for k in mapMat.index:
                if mapMat.loc[j][k] == 1:
                    dot.edge(str(j), str(k), fontname="Microsoft YaHei")
        pdfName = "resultDrawMap\\" + "第" + str(cluArray[numClu]) + "类" + i
        numClu = numClu + 1
        try:
            dot.view(filename=pdfName)
        except:
            pass
