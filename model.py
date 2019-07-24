#Accuracy is 0.371246
import os
import pandas as pd
import numpy as np
from sklearn import preprocessing, model_selection , svm
from sklearn.linear_model import LinearRegression

df = pd.read_csv('weather.csv', index_col=0)

df_1 = df.copy()
df_1.head()

df_1 = df_1.fillna(0)
df_1['RainTomorrow'].unique()

TrueFalse = {'Yes': 1,'No': 0, 0:-99999} 
df_1['RainToday'] = [TrueFalse[item] for item in df_1['RainToday']]
df_1['RainTomorrow'] = [TrueFalse[item] for item in df_1['RainTomorrow']]


dir_1 = list(df_1['WindGustDir'].unique())
dir_2 = list(df_1['WindDir9am'].unique())
dir_3 = list(df_1['WindDir3pm'].unique())
all_dir = dir_1 + dir_2 + dir_3
all_dir_dedup = list(set(all_dir))


dir_dict = {}
for num, winddir in enumerate(all_dir_dedup):
    dir_dict[winddir] = num


df_1['WindGustDir'] = df_1['WindGustDir'].map(dir_dict)
df_1['WindDir9am'] = df_1['WindDir9am'].map(dir_dict)
df_1['WindDir3pm'] = df_1['WindDir3pm'].map(dir_dict)
df_1.fillna(value = -99999, inplace=True)


df_1_noloc = df_1.drop(columns = ['Location'])
df_1_noloc = df_1_noloc[df_1_noloc.columns].astype(float)

x = np.array(df_1_noloc.drop(['RainTomorrow'], 1))
y = np.array(df_1_noloc['RainTomorrow'])
x = preprocessing.scale(x)
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

#Linear Regression Model
clf=LinearRegression()
clf.fit(x_train, y_train)
confidence = clf.score(x_test, y_test)
print(confidence)

#SVC
clf=svm.SVC()
clf.fit(x_train, y_train)
confidence = clf.score(x_test, y_test)
print(confidence)
