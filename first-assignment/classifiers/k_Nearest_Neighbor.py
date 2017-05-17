# -*-coding:utf8-*-
import numpy as np


class KNearestNeighbor(object):
    """
    K Nearest Neighbor Classifier
    输入一个K值
    计算每个分类的distances，选出最小的k个分类
    让这k个分类分别对测试数据进行投票，票数最高的分类获胜
    """

    def __init__(self):
        self.data_train = []
        self.label_train = []

    def train(self, X, y):
        """
        :param X: 训练集数据
        :param y: 训练集标签
        """
        self.data_train = X
        self.label_train = y
        pass

    def predict(self, X):
        """
        :param X: 测试集数据 
        :return: 测试集标签
        """
        length = X.shape[0]
        label_test = np.zeros(length, dtype=self.label_train.dtype)
        for i in xrange(length):
            print 'predict: %s'%i
            distances = np.sum(np.abs(self.data_train - X[i, :]), axis=1)
            min_index = np.argmin(distances)
            label_test[i] = self.label_train[min_index]
            print 'label:%s'%label_test[i]

        return label_test
