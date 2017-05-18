import numpy as np

x = np.array([0, 13, 10, 16, 20, 10, 15])

winner = []
bincount = np.bincount(x)
max_list = []
max_time = 0
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
    for i in x:
        if isbreak:
            break
        else:
            for j in max_list:
                if i == j:
                    winner = i
                    isbreak=1
elif len(max_list) == 1:
    winner = max_list[0]
else:
    print 'something wrong'

print winner
