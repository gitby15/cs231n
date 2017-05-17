# -*-coding:utf8-*-
import numpy as np


def unpickle(_file):
    import cPickle
    fo = open(_file, 'rb')
    dictionary = cPickle.load(fo)
    return dictionary


def load_cifar():
    """
    找到cifar的包，然后读取文件内容到内存
    :return: 返回训练集合测试集，并以numpy的数组形式返回
    """
    file_path = "../assets/cifar-10-batches-py"
    data_train = []
    label_train = []
    for i in range(1, 6):
        dic = unpickle(file_path + "/data_batch_" + str(i))
        for item in dic["data"]:
            data_train.append(item)
        for item in dic["labels"]:
            label_train.append(item)

    data_test = []
    label_test = []
    dic = unpickle(file_path + "/test_batch")
    for item in dic["data"]:
        data_test.append(item)
    for item in dic["labels"]:
        label_test.append(item)

    data_train = np.asarray(data_train)
    data_test = np.asarray(data_test)
    label_train = np.asarray(label_train)
    label_test = np.asarray(label_test)
    return data_train, label_train, data_test, label_test
