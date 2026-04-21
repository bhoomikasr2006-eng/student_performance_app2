import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("student_model.pkl", "rb"))

st.title("📚 Student Performance Prediction App")

study_hours = st.number_input("Study Hours")
attendance = st.number_input("Attendance (%)")
sleep_hours = st.number_input("Sleep Hours")
previous_marks = st.number_input("Previous Marks")
internet_usage = st.number_input("Internet Usage")
participation = st.number_input("Participation Level")

if st.button("Predict"):
    data = np.array([[study_hours, attendance, sleep_hours,
                      previous_marks, internet_usage, participation]])

    prediction = model.predict(data)

    st.success(f"Predicted Score: {prediction[0]:.2f}")
