# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the data set

train_set = pd.read_csv('train.csv')
test_set = pd.read_csv('train.csv')

from sklearn.preprocessing import LabelEncoder

train_set['Sex'] = LabelEncoder().fit_transform(train_set['Sex'])
test_set['Sex'] = LabelEncoder().fit_transform(test_set['Sex'])

#Training set data relavent
X_train = train_set.iloc[:, [2, 4, 5, 6, 7]].values
y_train = train_set.iloc[:, 1].values

#Test set data relevent
X_test = test_set.iloc[:, [2, 4, 5, 6, 7]].values
y_test = test_set.iloc[:, 1].values

#Imputeing the data in X_train
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit(X_train[:, 1:4])

X_train[:, 1:4] = imp_mean.fit_transform(X_train[:, 1:4])

#Imputeing data in X_test
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit(X_test[:, 1:4])

X_test[:, 1:4] = imp_mean.fit_transform(X_test[:, 1:4])



# Fitting Kernel SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

acc_log = round(classifier.score(X_train, y_train) * 100, 2)
acc_log


