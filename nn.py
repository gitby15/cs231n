# -*-coding:utf8-*-
import numpy as np

import util as util

datatr, labeltr, datate, labelte = util.load_CIFAR10()

Xtr = np.asarray(datatr)
Xte = np.asarray(datate)

Ytr = np.asarray(labeltr)
Yte = np.asarray(labelte)
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3)
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3)


class NearestNeighbor(object):
    def __init__(self):
        self.xtr = 0
        self.ytr = 0
        pass

    def train(self, X, y):
        """X is N x D where eachrow is an example. Y is 1-dimension of size N"""
        self.xtr = X
        self.ytr = y

    def predict(self, testData):
        """X is N x D where each row is an example we wish to predict label for"""
        num_test = testData.shape[0]
        Ypred = np.zeros(num_test, dtype=self.ytr.dtype)
        num = 0

        for i in xrange(num_test):
            """np.abs => self.xtr 中的每一行都去减testData[i, :]"""
            distances = np.sum(np.abs(self.xtr - testData[i, :]), axis=1)
            min_index = np.argmin(distances)
            Ypred[i] = self.ytr[min_index]
            num = num + 1
            if num % 10 == 0:
                print "num=", num / 10

        return Ypred

    def test(self, testData):
        print testData


nn = NearestNeighbor()
nn.train(Xtr_rows, Ytr)
Yte_predict = nn.predict(Xte_rows)
print 'accuracy: %f' % (np.mean(Yte_predict == Yte))
