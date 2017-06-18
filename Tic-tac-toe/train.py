# -*- coding: utf-8 -*-
# @Author: dieuson
# @Date:   2017-06-13 00:35:32
# @Last Modified by:   dieuson
# @Last Modified time: 2017-06-13 01:29:25

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.externals import joblib
import json


filename = "./data_set.json"
test_file = "./test.json"
with open(filename) as data_file:    
    dataset = json.load(data_file)

with open(test_file) as data_file:    
    data_test = json.load(data_file)

data = dataset["data"]
target = dataset["target"]

index = 8
inputs = data_test["data"][index]
response = data_test["target"][index]
print(data_test)


h = 0.5
x_min, x_max, y_min, y_max = -2, 2 + h, -2, 2 + h

xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))


#clf = linear_model.LinearRegression()
clf = svm.SVC(gamma=0.1, C=10)
res = clf.fit(data, target)


# Initialize graph parameters
# plt.xlabel('left')
# plt.ylabel('right')
# plt.xlim(xx.min(), xx.max())
# plt.ylim(yy.min(), yy.max())

# # Create the fit graph
# for x in data:
# 	plt.scatter(x[0], x[1])

print(clf.predict(inputs))
print("\n\nInput: %s, result => %s" % (inputs,  response))
#print(clf)
#plt.show()

# To save your model into a file
#joblib.dump(clf, 'Or_model.pkl', compress=9)

# To load your model
# model_name = "Or_model.pkl"
# model_clone = joblib.load(model_name)
# model.predict(test)
