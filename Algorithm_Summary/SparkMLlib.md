# Spark MLlib中算法总结

## 1. 线性模型  
### 1.1 二分类（Binary classification）  
二分类算法是将目标分为两个类别，正例和负例。MLlib中包含两种线性二分类算法：线性支持向量机（linear support vector machines）和逻辑回归（logistic regression）。对于这两种方法，MLlib支持L1和L2正则变体  

#### 1.1.1 线性支持向量机（SVMs）  
线性支持向量机（[SVMs](https://en.wikipedia.org/wiki/Support_vector_machine#Linear_SVM)）是用于大规模分类任务的标准方法，他的损失函数如下：  
$$ L(\mathbf{w};\mathbf{x},y):=max \\{ 0,1-y\mathbf{w^{T}} \mathbf{x} \\} $$
线性SVMs在默认情况下使用L2正则化，同时也可选L1正则，在这种情况下问题就变成线性问题。  
线性支持向量机算法输出SVM模型，输入一个未知的数据点$$$\mathbf{x}$$$，模型根据$$$\mathbf{w^T}\mathbf{x}$$$预测结果，默认情况下如果$$$\mathbf{w^T}\mathbf{x}>=0$$$则输出为正，否则为负。

#### 1.1.2 逻辑回归
逻辑回归在二分类中广泛应用，损失函数表示如下：$$L(\mathbf{w};\mathbf{x},y):=log(1+e^{-y\mathbf{w}^T \mathbf{x}})$$
逻辑回归算法输出为逻辑回归模型，给定一个数据点$$$\mathbf{x}$$$，模型运用逻辑方程进行预测$$f(z)={1\over 1-e^{-z}}$$
其中$$$z=\mathbf{w}^T \mathbf{x}$$$，默认情况下，如果$$$f(\mathbf(w)^Tx)>0.5$$$，则输出为正，否则为负，与线性支持向量机不同，逻辑回归模型的输出$$$f(z)$$$可以预测输出为正的概率。

#### 1.1.3 评价矩阵
针对二分类，MLlib支持一般的评价矩阵，包括precision,recall,F-measure,receiver operating characteristic(ROC),precision-recall curve, area under the curves(AUC)，AUC主要用来比较多个模型之间的表现，而precision/recall/F-measure主要用来在预测模型中确定合适的阈值。

```
# -*- coding:utf-8 -*-

from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from numpy import array
import pyspark

sc = pyspark.SparkContext()

# Parse data function
def parsePoint(line):
    values = [float(x) for x in line.split(' ')]
    return LabeledPoint(values[0], values[1:])

# Load data
data = sc.textFile('data/mllib/sample_svm_data.txt')
parsedData = data.map(parsePoint)

# Build the model
model = LogisticRegressionWithSGD.train(parsedData)

# Evaluating the model on training data
labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))

trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(parsedData.count())

print 'Training Error = ' + str(trainErr)
```
