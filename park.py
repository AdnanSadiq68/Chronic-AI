import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score

model = svm.SVC(kernel='linear')
scaler = StandardScaler()
def trainData():    
    parkinsons_data = pd.read_csv('parkinsons.csv')
    X = parkinsons_data.drop(columns=['name', 'status'], axis=1)
    Y = parkinsons_data['status']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)
    accuracy_logreg = accuracy_score(Y_test, Y_pred)
    print(accuracy_logreg*100)

trainData()
def testData(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = model.predict(std_data)
    if (prediction[0] == 0):
        output =  "NEGATIVE."
    else:
        output = "POSATIVE."
    return output