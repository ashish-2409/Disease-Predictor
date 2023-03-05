import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
import sys

# for p in sys.path:
#     print( p )
#reading the dataset
ds=pd.read_csv('C:/Users/Ashish/Desktop/Disease Predictor/Disease-Predictor/Dataset/dataset.csv')
# print(ds)

# deleting the last column extra value
del ds[ds.columns[-1]]
# print(ds.columns)

def get_columns():
    return ds.columns

#separating input and output vectors
input=ds.iloc[:,:-1]
target=ds.iloc[:,-1]
# print(input.shape)
# print(target.shape)

#splitting data into training and testing
x_train,x_test,y_train,y_test=train_test_split(input,target,test_size=0.2,random_state=10)
# print(x_train.shape,y_train.shape)
# print(x_test.shape,y_test.shape)
# print(target.shape)

#creating Decison tree classifier
classifier=DecisionTreeClassifier()

#training the modle
classifier.fit(x_train,y_train)

#making predictions
y_pred=classifier.predict(x_test)
# print(y_pred)
print(accuracy_score(y_test,y_pred)*100)
# print(confusion_matrix(y_test,y_pred))
# print(classification_report(y_test,y_pred))