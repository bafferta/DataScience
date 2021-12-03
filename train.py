import pandas
from sklearn import svm
from joblib import dump, load 
import matplotlib.pyplot as plt

df = pandas.read_csv("./pong_data.csv")
X = df[['ball_x','ball_y']]
print(X.shape)
y = df['paddle_y']
reg = svm.SVR()
reg.fit(X.values,y.values)

dump(reg, 'mymodel.joblib') #save  