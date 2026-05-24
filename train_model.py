import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Load dataset
df = pd.read_csv("data/student-por.csv")


# Convert final grade G3 into performance category
def convert_performance(score):
    if score < 10:
        return "Low"
    elif score <= 14:
        return "Medium"
    else:
        return "High"


df["performance"] = df["G3"].apply(convert_performance)


# These are the inputs we will ask in Streamlit app
selected_features = [
    "school", "sex", "age", "address",
    "Medu", "Fedu", "studytime", "failures",
    "schoolsup", "famsup", "paid", "activities",
    "higher", "internet", "romantic",
    "famrel", "freetime", "goout", "health",
    "absences", "G1", "G2"
]


X = df[selected_features]
y = df["performance"]


# Separate text columns and number columns
categorical_features = X.select_dtypes(include=["object"]).columns.tolist()
numeric_features = X.select_dtypes(exclude=["object"]).columns.tolist()


# Convert text to numbers and scale number values
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", StandardScaler(), numeric_features)
    ]
)


# Create model pipeline
model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", RandomForestClassifier(
            n_estimators=300,
            random_state=42,
            class_weight="balanced"
        ))
    ]
)


# Split data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Train the model
model.fit(X_train, y_train)


# Test the model
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# Save trained model
joblib.dump(model, "student_performance_model.pkl")

print("Model saved successfully!")