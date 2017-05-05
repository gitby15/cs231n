# -*-coding:utf8-*-
import util as index

(dtr, dte, ltr, lte) = index.load_CIFAR10()

# f(xi, W, b) = W * xi + b
# xi ∈ RD, 每个图像都有一个对应的分类标签yi
# N 个图像样例, 每个图像的纬度是D, 一共有K种不同的分类
#


# W -> 权重 是一个[K x D]的矩阵
# b -> 偏差向量 是一个[K x 1]的矩阵


dtr_len = dtr.shape[0]
for item in dtr:
    print type(item)
