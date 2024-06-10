import streamlit as st
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load dataset
housing = fetch_openml(name="house_prices", as_frame=True)
X = housing.data[["GrLivArea", "YearBuilt"]]  # Select a few features
y = housing.target

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit app
st.title('Ames Housing Price Prediction')

GrLivArea = st.number_input('Above grade living area in square feet', value=1500)
YearBuilt = st.number_input('Original construction date', value=2000)

input_data = pd.DataFrame({'GrLivArea': [GrLivArea], 'YearBuilt': [YearBuilt]})

if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Predicted House Price: ${prediction[0]:.2f}')
