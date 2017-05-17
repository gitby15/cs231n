# -*-coding:utf8-*-
from util import loadcifar as loader
from classifiers.k_Nearest_Neighbor import KNearestNeighbor

data_train, label_train, data_test, label_test = loader.load_cifar()

classifier = KNearestNeighbor()
# 训练分类器
classifier.train(data_train, label_train)
# 给数据进行分类
c_label_test = classifier.predict(data_test)

predict_right = 0
predict_wrong = 0

# 计算准确率
for i in range(0, label_test.shape[0]):
    if c_label_test[i] == label_test[i]:
        predict_right += 1
    else:
        predict_wrong += 1
# 输出结果
accuracy_rate = float(predict_right)/(predict_wrong+predict_right)
print 'right: [%s],false[%s]'%(predict_right,predict_wrong)
print 'accuracy rate is [%f]'%(accuracy_rate)



