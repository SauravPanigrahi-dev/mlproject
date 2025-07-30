import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("best_model.pkl")

st.set_page_config(page_title="Employee Salary Classification", page_icon="💼", layout="centered")

st.title("💼 Employee Salary Classification App")
st.markdown("Predict whether an employee earns >50K or ≤50K based on input features.")

# Sidebar inputs (these must match your training feature columns)
st.sidebar.header("Input Employee Details")

# ✨ Replace these fields with your dataset's actual input columns
age = st.sidebar.slider("Age", 18, 65, 30)

edu_map = {
    "10th": 0,
    "11th": 1,
    "12th": 2,
    "7th-8th":3,
    "9th":4,
    "Assoc-acdm":5,
    "Assoc-voc":6,
    "Bachelors":7,
    "Doctorate":8,
    "HS-grad": 9,
    "Masters":10,
    "Prof-school":11,
    "Some-college":12
}
education = st.sidebar.selectbox("Education Level", list(edu_map.keys()))
enc_edu = edu_map[education]


occ_map = {
    "Adm-clerical": 0,
    "Armed-Forces": 1,
    "Craft-repair": 2,
    "Exec-managerial":3,
    "Farming-fishing":4,
    "Handlers-cleaners":5,
    "Machine-op-inspct":6,
    "Other-service":7,
    "Others":8,
    "Priv-house-serv": 9,
    "Prof-specialty":10,
    "Protective-serv":11,
    "Sales":12,
    "Tech-support":13,
    "Transport-moving":14
}
occupation = st.sidebar.selectbox("Occupation", list(occ_map.keys()))
enc_occ = occ_map[occupation]


mar_map = {
    "Divorced": 0,
    "Married-AF-spouse": 1,
    "Married-civ-spouse": 2,
    "Married-spouse-absent":3,
    "Never-married":4,
    "Separated":5,
    "Widowed":6,
  
}
mar_status= st.sidebar.selectbox("Marital_status", list(mar_map.keys()))
enc_mar = mar_map[mar_status]

gen_map = {
    "Female": 0,
    "Male": 1,
}
gender= st.sidebar.selectbox("Gender", list(gen_map.keys()))
enc_gen = gen_map[gender]

cap_gain=st.number_input("Enter gains from other resources:",min_value=0, max_value=100000, step=1)
cap_loss=st.number_input("Enter losses from other resources:",min_value=0, max_value=100000, step=1)

hours_per_week = st.sidebar.slider("Hours per week", 1, 80, 40)



# Build input DataFrame (⚠️ must match preprocessing of your training data)
input_df = pd.DataFrame({
    'age': [age],
    'education': [enc_edu],
    'marital-status':[enc_mar],
    'occupation': [enc_occ],
    'gender':[enc_gen],
    'capital-gain':[cap_gain],
    'capital-loss':[cap_loss],
    'hours-per-week': [hours_per_week]

})

st.write("### 🔎 Input Data")
st.write(input_df)

# Predict button
if st.button("Predict Salary Class"):
    prediction = model.predict(input_df)
    st.success(f"✅ Prediction: {prediction[0]}")
