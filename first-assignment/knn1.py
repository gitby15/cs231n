# -*-coding:utf8-*-
from assignment1.k_Nearest_Neighbor import KNearestNeighbor
from util import loadcifar as loader

data_train, label_train, data_test, label_test = loader.load_cifar()


def cifar_reshape(train_size, test_size):
    return data_train[0:train_size], label_train[0:train_size], data_test[0:test_size], label_test[0:test_size]


data_train, label_train, data_test, label_test = cifar_reshape(2200, 500)

classifier = KNearestNeighbor()
# 训练分类器
classifier.train(data_train, label_train)

classifier.changek(5)
# 给数据进行分类
c_label_test = classifier.predict(data_test)

predict_right = 0
predict_wrong = 0

# 计算准确率
print c_label_test
print label_test[0:1000]
for i in range(label_test.shape[0]):
    if c_label_test[i] == label_test[i]:
        predict_right += 1
    else:
        predict_wrong += 1
# 输出结果
accuracy_rate = float(predict_right) / (predict_wrong + predict_right)
print 'right: [%s],false[%s]' % (predict_right, predict_wrong)
print 'accuracy rate is [%f]' % (accuracy_rate)
