概念图分析方案
1.	任务一：概念图聚类
使用DBSCAN和谱分类两种方式对收集到的学生概念进行聚类，对比两种方法聚类结果的差异，具体包括两个子任务：
（1）	将学生本门课程完成的所有概念图进行聚类，了解学生在C语言课程中的绘图的分类。
（2）	将学生本门课程的概念图按照章节进行聚类（因为对本学期所有概念图进行聚类，聚类结果肯能会受到绘图的主题影响）。
2.	任务二：利用社会网络分析方法分析学生期中与期末概念图
学生期中及期末的概念图使用的固定的概念，在绘图过程中可能增加部分新的概念，因此应该大部分概念是重复的概念。
（1）	读取期中测试中所有概念图的出现的概念，并对概念进行聚类
（2）	把学生的概念图转化为矩阵表
（3）	把期中测试中所有学生的矩阵表相加，得到群体矩阵表
（4）	把群体矩阵表作为社会网络分析的输入，分析网络中心度、密度
（5）	按照1-4的方法，把期末的概念图数据处理一遍
（6）	对比期末和期中的数据区别
参考文献：
2013-Concept maps as network data: Analysis of a concept map using the methods of social network analysis
3.	任务三：读取期中和期末学生概念图的以下结构指标
广度指标	节点个数、叶节点个数、分支个数（概念图中分支）、最大层宽度、等级关系的个数、交叉关系的个数、总宽度、平均宽度、信息熵总和、非叶子节点的平均信息熵
深度指标	层数、最大叶节点深度、叶节点深度总和、根节点到叶节点的路径总条数、平均叶子深度、路径总深度、路径总条数、平均路径深度
网络指标	知识存储容量S=H/A、知识分布性D=log(T*H(1-A)和知识检索R=√(S*P)、表面结构、图形结构、连通性、强度、节点平均度数、循环、循环次数、至高点

参考文献：
1）2006-概念地图及其结构分析在知识评价中的应用（三）：实证研究
2）2020- The network approach to assess the structure of knowledge: Storage, distribution and retrieval as three measures in analysing concept maps
3）2011-The mystery of cognitive structure and how we can detect it: tracking the development of cognitive structures over time

