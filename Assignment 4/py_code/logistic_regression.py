import numpy as np
import os
from random import shuffle


# predict in our case predict male/female.
def predict(x):
    if x >= 0.5:
        return 1
    else:
        return 0


# we found this normalization to be superior in our case
# normalization x=(x-mean(x))/(max(x)-min(x))
def normalize1(x):
    mu = np.mean(x)
    smin = np.amin(x)
    smax = np.amax(x)
    x = (x - mu) / (smax - smin)
    return x


# we found this normalization inferior in our case
# normalization x=(x-mean(x))/std(x)
def normalize2(x):
    x = (x - x.mean()) / x.std()
    return x


def sigmoid(w, x, b_vec):
    return 1 / (1 + np.exp(-(np.dot(w, x) + b_vec)))


# path to file
path = os.getcwd() + "/../data/data set.txt"

# read file and replace the string data in its numerical representation
with open(path) as f:
    lines = f.readlines()
    for idx, line in enumerate(lines):
        lines[idx] = str(lines[idx]).replace('female', str(0))
        lines[idx] = str(lines[idx]).replace('male', str(1))
        lines[idx] = str(lines[idx]).replace('full', str(3))
        lines[idx] = str(lines[idx]).replace('associate', str(2))
        lines[idx] = str(lines[idx]).replace('assistant', str(1))
        lines[idx] = str(lines[idx]).replace('doctorate', str(1))
        lines[idx] = str(lines[idx]).replace('masters', str(0))
        lines[idx] = str(lines[idx]).replace('\n', '')

# shuffle data
shuffle(lines)

# prepare data
data = [[num for num in line.split('	')] for line in lines]
dim = len(data[0])
data = np.array(data, dtype=float)

# remove data from results
Y = np.delete(data, np.r_[1:7], axis=1)
data = np.insert(data, np.r_[0:1], np.ones([len(data), 1]), axis=1)

# remove results from data
X = np.delete(data, np.r_[1:2], axis=1)
data = np.insert(data, np.r_[0:1], np.ones([len(data), 1]), axis=1)

arrayL = []
arrayM = []

# add features, data set is too small to determine if adding features is beneficial, we've had mixed results.
# for i in range(0,len(X)):
#     if(int(X[i][4])>=30000):
#         arrayM.append(1)
#     else:
#         arrayM.append(0)
#     if(int(X[i][4])<=20000):
#         arrayL.append(1)
#     else:
#         arrayL.append(0)
# X = np.column_stack((X,np.array(arrayL)))
# X = np.column_stack((X,np.array(arrayM)))

# normalizer the data
X = normalize2(X)
# prepare test batch 30% data
test_x = np.delete(X, np.r_[len(X) * 0.3:len(X)], axis=0)
test_y = np.delete(Y, np.r_[len(Y) * 0.3:len(Y)], axis=0)

# prepare train batch 70% data
data_x = np.delete(X, np.r_[0:len(X) * 0.3], axis=0)
data_y = np.delete(Y, np.r_[0:len(Y) * 0.3], axis=0)

data_y = np.array([int(num) for num in data_y])

# weight vector initialized to zero
W = np.zeros(len(X[0]), dtype=float)
# b initialized to zero
b = 0

# train batch 100k iterations,LR=0.005

for i in range(0, 100000):
    gradient_b = np.mean(1 * (data_y - (sigmoid(data_x, W, data_y))))
    gradient_w = np.dot(np.array((data_y - sigmoid(data_x, W, b))), np.array(data_x)) * 1 / len(data_y)
    b += 0.005 * gradient_b
    W += 0.005 * gradient_w

TP = 0
TN = 0
FN = 0
FP = 0

# test batch
for i in range(0, len(test_y)):
    pred = predict(sigmoid(np.array(test_x[i]), W, b))
    if pred == 1 and test_y[i] == 1:
        TP += 1
    if pred == 0 and test_y[i] == 0:
        TN += 1
    if pred == 0 and test_y[i] == 1:
        FN += 1
    if pred == 0 and test_y[i] == 1:
        FP += 1

if __name__ == "__main__":
    accuracy = (1. * TP + 1. * TN) / (1. * len(test_y))

    precision = 1. * TP / (1. * TP + 1. * FP)

    recall = 1. * TP / (1. * TP + 1. * FN)

    F1 = 2. * precision * recall / (1. * precision + 1. * recall)
    print("TP: ", TP, " TN: ", TN, " FN: ", FN, " FP: ", FP)
    print("accuracy: ", accuracy, " precision: ", precision, " recall: ", recall, " F1: ", F1)
