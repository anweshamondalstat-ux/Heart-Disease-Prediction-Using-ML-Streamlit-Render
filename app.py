import streamlit as st
import pandas as pd
import numpy as np
import pickle



st.title("Heart Disease Predictor")

tab1, tab2 = st.tabs(['Predict', 'Model Information'])

with tab1:
   

    age = st.number_input("Age (years)", min_value=0, max_value=150)
    sex = st.selectbox("Sex", ["Male", "Female"])

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"]
    )

    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300)
    cholesterol = st.number_input("Serum Cholesterol (mm/dl)", min_value=0)

    fasting_bs = st.selectbox("Fasting Blood Sugar", ["<= 120 mg/dl", "> 120 mg/dl"])
    resting_ecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])

    max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220)

    exercise_angina = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])

    oldpeak = st.number_input("Oldpeak (ST Depression)", min_value=0.0, max_value=10.0)

    st_slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])

    # 🔹 Encoding
    sex_val = 0 if sex == "Male" else 1
    chest_pain_val = ["Atypical Angina", "Non-Anginal Pain", "Asymptomatic", "Typical Angina"].index(chest_pain)
    fasting_bs_val = 1 if fasting_bs == "> 120 mg/dl" else 0
    resting_ecg_val = ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"].index(resting_ecg)
    exercise_angina_val = 1 if exercise_angina == "Yes" else 0
    st_slope_val = ["Upsloping", "Flat", "Downsloping"].index(st_slope)


# 🔹 Create DataFrame (MATCH TRAINING DATA EXACTLY)
    input_data = pd.DataFrame({
        'Age': [age],
        'Sex': [sex_val],
        'ChestPainType': [chest_pain_val],
        'RestingBP': [resting_bp],
        'Cholesterol': [cholesterol],
        'FastingBS': [fasting_bs_val],
        'RestingECG': [resting_ecg_val],
        'MaxHR': [max_hr],
        'ExerciseAngina': [exercise_angina_val],
        'Oldpeak': [oldpeak],
        'ST_Slope': [st_slope_val]
    })
# Algorithm names
algonames = ['Decision Trees', 'Logistic Regression', 'Random Forest', 'Support Vector Machine']

# Model file names
modelnames = ['DecisionTree.pkl', 'LogisticR.pkl', 'RandomForest.pkl', 'SVM.pkl']

predictions = []

def predict_heart_disease(data):
    for modelname in modelnames:
        model = pickle.load(open(modelname, 'rb'))
        prediction = model.predict(data)
        predictions.append(prediction[0])
    return predictions


#create a submit button to make prediction
if st.button("Submit"):
    st.subheader('Results....')
    st.markdown('--------------')

    result = predict_heart_disease(input_data)

    for i in range(len(result)): 
        st.subheader(algonames[i])

        if result[i] == 0:   
            st.write("No heart disease detected.")
        else:
            st.write("Heart disease detected")

        st.markdown('------------') 


with tab2:
    import plotly.express as px
    data={'Decision Trees': 80.97, 'Logistic Regression': 85.86, 'SVM':83.16,'Random Forest': 86.41}
    Models = list(data.keys())
    Accuracies= list(data.values())
    df2 = pd.DataFrame(list(zip(Models, Accuracies)), columns=['Models', 'Accuracies'])
    fig= px.bar(df2, y='Accuracies',x='Models')
    st.plotly_chart(fig)
     

       