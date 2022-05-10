# -*- coding: utf-8 -*-
"""
Created on Sun May  1 13:57:24 2022

@author: kaieu
"""
#1
from sklearn.datasets import load_wine
import pandas as pd
wine=load_wine()
#2
#This dataset is about the different properties of wine and what they would be clasified as.
#The goal of machine learning with this dataset is how a machine can \
#predict different properties based on other properties provided or what 
#category a wine would fall in based on its properies
#3
df_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
df_wine['class']=wine.target
pd.set_option('max_columns',14)
df_wine.head(3)
#4
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
x_train,x_test,y_train,y_test = train_test_split(wine.data,wine.target)
for k in range(1,22,2):
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    accuracy = knn.score(x_test,y_test)
    print(f'K={k}, score={accuracy:.2%}')
#Based on the loop, 1 and 3 are equally as accurate
from sklearn.metrics import confusion_matrix
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
predicted = knn.predict(x_test)
confusion = confusion_matrix(y_test,predicted)
print(confusion)
#The matrix states that the prediction model analyzed 15 of the first
#category and got 14 right and 0 wrong. The prediction model analyzed 15 of the
#second category and got 11 right and 4 wrong. In the last category,
# it got 4 right and 11 wrong. 




from sklearn.model_selection import KFold
kf = KFold(10)
for k in range(1,22,2):
    knn=KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn,wine.data,wine.target,cv=kf)
    avg_score = scores.mean()
    print(f'K={k}, average accuracy={avg_score:.2%}')
#based on the for loop 1 neighbor is the best for this dataset
#5
from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier()
x_train,x_test,y_train,y_test = train_test_split(wine.data,wine.target)
dt.fit(x_train,y_train)
print(dt.score(x_test,y_test))
from sklearn.tree import export_graphviz
export_graphviz(dt,out_file=('digits.dot'),feature_names=wine.feature_names,class_names=wine.target_names,filled=True)
scores = cross_val_score(dt,wine.data,wine.target,cv=kf)
print(scores.mean())
#The decision tree performs better when working with the wine dataset

#6
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3)
km.fit(wine.data)
print(km.labels_)
print(km.cluster_centers_)