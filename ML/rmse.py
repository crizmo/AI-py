import numpy as np
from sklearn.linear_model import LinearRegression

X_train = np.array([43, 21, 25, 42, 57, 59]).reshape((-1, 1))
Y_train = np.array([99, 65, 79, 75, 87, 81])

model = LinearRegression()
model.fit(X_train, Y_train)

age_to_predict = np.array([55]).reshape((-1, 1))

glucose_level_prediction = model.predict(age_to_predict)

print("Predicted glucose level:", glucose_level_prediction)
