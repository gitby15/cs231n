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
        self.k = 1
        pass

    def train(self, X, y):
        """
        :param X: 训练集数据
        :param y: 训练集标签
        """
        self.data_train = X
        self.label_train = y
        pass

    def changek(self, k=1):
        self.k = k
        pass

    def predict(self, X):
        """
        :param X: 测试集数据 
        :return: 测试集标签
        """
        length = X.shape[0]
        label_list = np.zeros((length, self.k), dtype=self.label_train.dtype)
        for i in xrange(length):
            print 'predict: %s' % i
            distances = np.sum(np.abs(self.data_train - X[i, :]), axis=1)
            min_index_list = np.argsort(distances)
            for j in xrange(self.k):
                label_list[i][j] = self.label_train[min_index_list[j]]
                pass
            pass
        label_test = self.__vote(label_list)
        return label_test

    def __vote(self, label_list):
        """
        选出出现频率最高的标签，如果频率相等，选出index最小的标签
        :param label_list: 每张图片的k个标签
        :return: 投票结果
        """
        print 'run to here'
        length = label_list.shape[0]
        label_test = np.zeros(length, dtype=self.label_train.dtype)
        for x in xrange(length):
            bincount = np.bincount(label_list[x])
            max_list = []
            max_time = 0
            winner = 0
            for i in xrange(bincount.shape[0]):
                if bincount[i] > max_time:
                    max_list = []
                    max_list.append(i)
                    max_time = bincount[i]
                    pass
                elif bincount[i] == max_time:
                    max_list.append(i)
                pass

            isbreak = 0
            if len(max_list) > 1:
                # print 'max_list'
                # print max_list
                for i in label_list[x]:
                    if isbreak:
                        break
                    else:
                        for j in max_list:
                            if i == j:
                                winner = i
                                isbreak = 1
            elif len(max_list) == 1:
                winner = max_list[0]
            else:
                print 'something wrong'

            label_test[x] = winner
            pass

        return label_test
