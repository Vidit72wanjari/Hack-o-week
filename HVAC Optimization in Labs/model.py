import joblib
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from data_generator import generate_data


def train_model():

    data = generate_data()

    X = data[["Occupancy","Indoor_Temp","Outdoor_Temp"]]
    y = data["Cooling_Load"]

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

    model = DecisionTreeRegressor(max_depth=5)
    model.fit(X_train,y_train)

    joblib.dump(model,"hvac_model.pkl")

    return model


def load_model():

    try:
        model = joblib.load("hvac_model.pkl")
    except:
        model = train_model()

    return model