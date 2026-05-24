import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("student_performance_model.pkl")


st.title("🎓 Student Performance Prediction System")

st.write("Enter student details and predict whether the student performance is Low, Medium, or High.")


st.subheader("Basic Details")

school = st.selectbox("School", ["GP", "MS"])
sex = st.selectbox("Gender", ["F", "M"])
age = st.slider("Age", 15, 22, 17)
address = st.selectbox("Address Type", ["U", "R"])


st.subheader("Family and Study Details")

Medu = st.selectbox("Mother's Education Level", [0, 1, 2, 3, 4])
Fedu = st.selectbox("Father's Education Level", [0, 1, 2, 3, 4])
studytime = st.selectbox("Weekly Study Time", [1, 2, 3, 4])
failures = st.selectbox("Past Class Failures", [0, 1, 2, 3])


st.subheader("Support Details")

schoolsup = st.selectbox("School Support", ["yes", "no"])
famsup = st.selectbox("Family Support", ["yes", "no"])
paid = st.selectbox("Extra Paid Classes", ["yes", "no"])
activities = st.selectbox("Extra-curricular Activities", ["yes", "no"])
higher = st.selectbox("Wants Higher Education", ["yes", "no"])
internet = st.selectbox("Internet Access", ["yes", "no"])
romantic = st.selectbox("In Relationship", ["yes", "no"])


st.subheader("Lifestyle and Academic Details")

famrel = st.slider("Family Relationship Quality", 1, 5, 4)
freetime = st.slider("Free Time", 1, 5, 3)
goout = st.slider("Going Out with Friends", 1, 5, 3)
health = st.slider("Health Status", 1, 5, 4)
absences = st.slider("Absences", 0, 32, 2)
G1 = st.slider("First Period Grade G1", 0, 20, 10)
G2 = st.slider("Second Period Grade G2", 0, 20, 10)


if st.button("Predict Performance"):

    input_data = pd.DataFrame({
        "school": [school],
        "sex": [sex],
        "age": [age],
        "address": [address],
        "Medu": [Medu],
        "Fedu": [Fedu],
        "studytime": [studytime],
        "failures": [failures],
        "schoolsup": [schoolsup],
        "famsup": [famsup],
        "paid": [paid],
        "activities": [activities],
        "higher": [higher],
        "internet": [internet],
        "romantic": [romantic],
        "famrel": [famrel],
        "freetime": [freetime],
        "goout": [goout],
        "health": [health],
        "absences": [absences],
        "G1": [G1],
        "G2": [G2]
    })

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == "High":
        st.success("High Performance Student")
        st.write("Suggested Action: Give advanced learning tasks and skill-based challenges.")

    elif prediction == "Medium":
        st.warning("Medium Performance Student")
        st.write("Suggested Action: Give regular practice, revision support, and guided improvement.")

    else:
        st.error(" Low Performance Student")
        st.write("Suggested Action: Give basic revision, mentoring support, and extra learning material.")