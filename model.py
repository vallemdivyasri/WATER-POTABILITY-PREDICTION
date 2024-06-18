import pickle

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data = pd.read_csv("water_potability.csv")

print(data.info())

data.fillna(data.mean(), inplace=True)

x = data.drop("Potability", axis=1)

y = data["Potability"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

import sklearn.ensemble
from sklearn.ensemble import RandomForestClassifier

d = sklearn.ensemble.RandomForestClassifier(random_state=10)
d.fit(x_train, y_train)

pickle.dump(d,open('model.pkl','wb'))
