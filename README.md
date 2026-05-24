# stud-perf-pred

## Project Overview

This project is a Machine Learning-based web application that predicts a student's performance level as Low, Medium, or High.

The system takes student details such as school, gender, age, study time, family support, internet access, previous grades, absences, and lifestyle details. Based on these inputs, the trained ML model predicts the final performance category.

The application is built using Python, Scikit-learn, and Streamlit.

---

## Dataset

The dataset used is `student-por.csv`.

It contains student academic, family, social, and lifestyle-related information.

Important grade columns:

- G1: First period grade
- G2: Second period grade
- G3: Final grade

In this project, G3 is converted into a performance category.

---

## Performance Category

The final grade G3 is converted as:

```text
G3 < 10       -> Low Performance
G3 10 to 14   -> Medium Performance
G3 >= 15      -> High Performance
````

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Random Forest Classifier
* Streamlit
* Joblib

---

## Project Workflow

```text
Dataset
   ↓
Data preprocessing
   ↓
Feature selection
   ↓
Model training
   ↓
Model evaluation
   ↓
Model saving
   ↓
Streamlit web app
   ↓
User input prediction
```

---

## Features Used for Prediction

The model uses the following features:

* School
* Gender
* Age
* Address type
* Mother’s education
* Father’s education
* Study time
* Past failures
* School support
* Family support
* Paid classes
* Activities
* Higher education interest
* Internet access
* Relationship status
* Family relationship quality
* Free time
* Going out
* Health
* Absences
* G1 grade
* G2 grade

---

## Machine Learning Model

The model used is:

```text
Random Forest Classifier
```

A Scikit-learn pipeline is used with:

* OneHotEncoder for categorical values
* StandardScaler for numerical values
* RandomForestClassifier for prediction

---

## How to Run the Project

### 1. Install required libraries

```bash
python -m pip install pandas scikit-learn streamlit joblib
```

### 2. Train the model

```bash
python train_model.py
```

This will create the model file:

```text
student_performance_model.pkl
```

### 3. Run the Streamlit app

```bash
python -m streamlit run app.py
```

---

## Output

The app predicts one of the following results:

* Low Performance Student
* Medium Performance Student
* High Performance Student

It also provides a basic improvement suggestion based on the prediction.

---

## Project Use Case

This project can be useful for early identification of students who may need academic support. Teachers or mentors can use the prediction result to provide personalized guidance, revision support, or advanced learning activities.

---

## Future Improvements

* Add prediction confidence chart
* Improve UI design
* Add more student-friendly suggestions
* Deploy the app online
* Use a larger dataset
* Add recommendation system for skill improvement

```
---
##screenshots
<img width="1696" height="894" alt="image" src="https://github.com/user-attachments/assets/dc2407e8-cc40-4e0a-9746-e408baaa88c3" />
<img width="1781" height="899" alt="image" src="https://github.com/user-attachments/assets/d48fdbca-cab2-4777-9c83-c37568504263" />
<img width="1500" height="877" alt="image" src="https://github.com/user-attachments/assets/ce5481f9-8c10-421d-889f-0871ae736e54" />
<img width="1361" height="886" alt="image" src="https://github.com/user-attachments/assets/987ab1ff-fdfe-474b-a2dd-9e53d2065e32" />
