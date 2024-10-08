# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FpnMlP2wbrqyYLlKmIRAHmriAc-1s_c-
"""

# prompt: import pandas

import pandas as pd

# prompt: import /content/Riya Maithani - revolutioncart_data.csv

import pandas as pd
df = pd.read_csv('/content/Riya Maithani - revolutioncart_data.csv')

df

# prompt: consider monthly_revenue as y and rest as X

X = df.drop('monthly_revenue', axis=1)
y = df['monthly_revenue']

# prompt: split the data into X_train and y_train

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# prompt: create model linear regression

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# prompt: predict the accuracy and analyse the model

from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Analyze the model
# You can examine the coefficients of the model to understand the relationship between
# each feature and the target variable.
print("Coefficients:", model.coef_)

# You can also create a scatter plot of the predicted values vs. the actual values to
# visually assess the model's performance.
import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Monthly Revenue")
plt.ylabel("Predicted Monthly Revenue")
plt.title("Actual vs. Predicted Monthly Revenue")
plt.show()

# prompt: do cross validation and do the predictions

import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_predict

# Perform cross-validation and get predictions
y_pred_cv = cross_val_predict(model, X, y, cv=5)  # Use 5-fold cross-validation

# Evaluate the model with cross-validated predictions
mse_cv = mean_squared_error(y, y_pred_cv)
r2_cv = r2_score(y, y_pred_cv)

print(f"Mean Squared Error (Cross-validated): {mse_cv}")
print(f"R-squared (Cross-validated): {r2_cv}")

# You can also create a scatter plot of the cross-validated predicted values vs. the actual values
plt.scatter(y, y_pred_cv)
plt.xlabel("Actual Monthly Revenue")
plt.ylabel("Predicted Monthly Revenue (Cross-validated)")
plt.title("Actual vs. Predicted Monthly Revenue (Cross-validated)")
plt.show()

# prompt: dump the model

import pickle

# Save the model to a file
filename = 'linear_regression_model.sav'
pickle.dump(model, open(filename, 'wb'))

# Commented out IPython magic to ensure Python compatibility.
# # prompt: generate code for streamlit app
# 
# %%writefile nowapp.py
# import streamlit as st
# import pandas as pd
# import pickle
# 
# # Load the trained model
# filename = 'linear_regression_model.sav'
# model = pickle.load(open(filename, 'rb'))
# 
# # Create the Streamlit app
# st.title("Monthly Revenue Prediction")
# 
# # Create input fields for the features
# st.sidebar.header("Input Features")
# # Replace 'feature1', 'feature2', etc. with the actual feature names from your dataset
# feature1 = st.sidebar.number_input("Feature 1")
# feature2 = st.sidebar.number_input("Feature 2")
# # Add more input fields for other features as needed
# 
# # Create a button to make the prediction
# if st.sidebar.button("Predict"):
#     # Create a DataFrame with the input values
#     input_data = pd.DataFrame([[feature1, feature2]], columns=['feature1', 'feature2'])
# 
#     # Make the prediction
#     prediction = model.predict(input_data)[0]
# 
#     # Display the prediction
#     st.header("Predicted Monthly Revenue")
#     st.write(f"The predicted monthly revenue is: {prediction:.2f}")
# 
#