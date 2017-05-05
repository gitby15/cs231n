import numpy as np
def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    return dict


def load_CIFAR10():
    file = "./assets/cifar-10-batches-py"
    dataTrain = []
    labelTrain = []
    for i in range(1, 6):
        dic = unpickle(file + "/data_batch_" + str(i))
        for item in dic["data"]:
            dataTrain.append(item)
        for item in dic["labels"]:
            labelTrain.append(item)

    dataTest = []
    labelTest = []
    dic = unpickle(file + "/test_batch")
    for item in dic["data"]:
        dataTest.append(item)
    for item in dic["labels"]:
        labelTest.append(item)

    dataTrain = np.asarray(dataTrain)
    dataTest = np.asarray(dataTest)
    labelTrain = np.asarray(labelTrain)
    labelTest = np.asarray(labelTest)
    return (dataTrain, labelTrain, dataTest, labelTest)