# heart disease prediction
import numpy as np
# library for data processing
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
scale=StandardScaler()
randfor = RandomForestClassifier(n_estimators=100, random_state=0)
def trainData():
  data = pd.read_csv("diabetes.csv")
  predictors = data.drop("Outcome",axis=1)
  target = data["Outcome"]
  X_train,X_test,Y_train,Y_test = train_test_split(predictors,target,test_size=0.20,random_state=0)
  scale.fit(X_train)
  X_train=scale.transform(X_train)
  X_test=scale.transform(X_test)
  randfor.fit(X_train, Y_train)
  y_pred_rf = randfor.predict(X_test)
  print(y_pred_rf)
  accuracy_logreg = accuracy_score(Y_test, y_pred_rf)
  print(accuracy_logreg*100)
trainData()
def testData_diabetes(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    std_data = scale.transform(input_data_reshaped)
    prediction = randfor.predict(std_data)
    if (prediction[0] == 0):
        output =  "The person is not suffering from Diabetes."
    else:
        output = "The person is suffering from Diabetes."
    return output
