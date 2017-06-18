# -*- coding: utf-8 -*-
# @Author: dieuson
# @Date:   2017-06-13 01:34:09
# @Last Modified by:   dieuson
# @Last Modified time: 2017-06-13 22:51:46

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
import json

# To load your model
model_name = "model_detect_winner_tictactoe.pkl"
model = joblib.load(model_name)

test_file = "./Dataset/test.json"
with open(test_file) as data_file:    
    data_test = json.load(data_file)

nb_positive = 0
nb_negative = 0
index = 0

while index < 100:
	inputs = np.array(data_test["data"][index])
	inputs = inputs.reshape(1, -1)
	response = data_test["target"][index]
	prediction = model.predict(inputs)

	if (prediction == response):
		print("Greate")
		nb_positive += 1
	else:
		print("CHeat")
		nb_negative += 1
	index += 1

print("Positive: %d, Negative: %d, Total: %d" % (nb_positive, nb_negative, index))