# -*- coding: utf-8 -*-
# @Author: dieuson
# @Date:   2017-06-13 01:34:09
# @Last Modified by:   dieuson
# @Last Modified time: 2017-06-14 23:33:39

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
import json

# To load your model
model_name = "./Models/model_policy.pkl"
model = joblib.load(model_name)

filename = "./Test/test_policy.json"
with open(filename) as data_file:    
    test = json.load(data_file)

nb_positive = 0
nb_negative = 0
for x in xrange(1,1000):
	test_test = np.array(test["data"][x])
	test_test = test_test.reshape(1, -1)
#	print(test_test.reshape(1, -1))
	if (model.predict(test_test) == test["target"][x]):
		nb_positive += 1
	else:
		nb_negative += 1

print("Positive: %d, Negative: %d, Total: %d" % (nb_positive, nb_negative, x))