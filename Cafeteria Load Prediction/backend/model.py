import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("cafeteria_data.csv")

X = data[['temperature','humidity','weekday','hour']]
y = data['cafeteria_load']

model = LinearRegression()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))

print("Model trained successfully")