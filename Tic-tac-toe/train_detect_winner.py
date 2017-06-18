# -*- coding: utf-8 -*-
# @Author: dieuson
# @Date:   2017-06-13 00:35:32
# @Last Modified by:   dieuson
# @Last Modified time: 2017-06-13 22:51:31

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.externals import joblib
import json


filename = "./Dataset/dataset_detect_winner.json"
with open(filename) as data_file:    
    dataset = json.load(data_file)

data = np.array(dataset["data"])
target = np.array(dataset["target"])

h = 0.5
x_min, x_max, y_min, y_max = -2, 2 + h, -2, 2 + h

xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

#clf = linear_model.LinearRegression()
clf = svm.SVC(gamma=0.1, C=10)
res = clf.fit(data, target)

# To save your model into a file
joblib.dump(clf, 'model_detect_winner_tictactoe.pkl', compress=9)

# To load your model
# model_name = "Or_model.pkl"
# model_clone = joblib.load(model_name)
# model.predict(test)
