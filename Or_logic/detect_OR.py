# -*- coding: utf-8 -*-
# @Author: dieuson
# @Date:   2017-06-11 23:15:43
# @Last Modified by:   dieuson
# @Last Modified time: 2017-06-13 00:16:22

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.externals import joblib


dataset = {"a": [0, 0, 1, 1], "b": [0, 1, 0, 1], "output": [0, 1, 1, 1]}

a = dataset["a"]
b = dataset["b"]

h = 0.5
x_min, x_max, y_min, y_max = -2, 2 + h, -2, 2 + h

xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

inputs = 	[[0, 0],
			[0, 1],
			[1, 0],
			[1, 1],]

output = dataset["output"]

#clf = linear_model.LinearRegression()
clf = svm.SVC(gamma=0.1, C=100)
res = clf.fit(inputs,output)

test = [[0, 0]]

# Initialize graph parameters
plt.xlabel('left')
plt.ylabel('right')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

# Create the fit graph
for x in inputs:
	plt.scatter(x[0], x[1])


print(clf.predict(test))
#print(clf)
#plt.show()

# To save your model into a file
joblib.dump(clf, 'Or_model.pkl', compress=9)

# To load your model
# model_name = "Or_model.pkl"
# model_clone = joblib.load(model_name)
# model.predict(test)
