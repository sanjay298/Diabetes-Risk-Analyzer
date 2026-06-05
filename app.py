import streamlit as st
import joblib
from report_generator import generate_pdf

# Load trained model
model = joblib.load("model/diabetes_model.pkl")

# Page Title
st.title("🩺 Diabetes Risk Analyzer")
st.write("Enter your health details below")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, step=1)
glucose = st.number_input("Glucose Level", min_value=0.0)
blood_pressure = st.number_input("Blood Pressure", min_value=0.0)
skin_thickness = st.number_input("Skin Thickness", min_value=0.0)
insulin = st.number_input("Insulin Level", min_value=0.0)
bmi = st.number_input("BMI", min_value=0.0)

dpf = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    format="%.3f"
)

age = st.number_input("Age", min_value=1, step=1)

# Predict button
if st.button("Predict"):

    data = [[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age
    ]]

    # Prediction
    prediction = model.predict(data)[0]

    # Probability
    probability = model.predict_proba(data)[0][1]

    # Result Section
    st.subheader("Prediction Result")

    risk_percent = probability * 100
    st.write(f"Diabetes Risk Probability: {risk_percent:.2f}%")

    if risk_percent < 30:
        st.success("🟢 Low Risk")
    elif risk_percent < 70:
        st.warning("🟡 Moderate Risk")
    else:
        st.error("🔴 High Risk")

    # Recommendations
    st.subheader("📋 Personalized Recommendations")

    recommendations = []

    if glucose > 140:
        recommendations.append(
            "Reduce sugar intake and monitor blood glucose regularly."
        )

    if bmi > 25:
        recommendations.append(
            "Maintain a healthy weight through diet and exercise."
        )

    if blood_pressure > 80:
        recommendations.append(
            "Monitor blood pressure and reduce salt consumption."
        )

    if age > 45:
        recommendations.append(
            "Schedule regular diabetes screening checkups."
        )

    if insulin > 180:
        recommendations.append(
            "Consult a healthcare professional regarding insulin levels."
        )

    if len(recommendations) == 0:
        st.success(
            "Great! Your health indicators appear to be within healthy ranges."
        )
    else:
        for recommendation in recommendations:
            st.write("✅", recommendation)
    # Health Score Calculation
    health_score = 100

    if glucose > 140:
        health_score -= 25

    if bmi > 25:
        health_score -= 20

    if blood_pressure > 80:
        health_score -= 15

    if age > 45:
        health_score -= 10

    if insulin > 180:
        health_score -= 10

# Prevent negative score
    health_score = max(0, health_score)

    st.subheader("🏥 Health Score")

    st.metric(
        label="Overall Health Score",
        value=f"{health_score}/100"
)

    if health_score >= 80:
        st.success("Excellent Health Status")
    elif health_score >= 60:
        st.warning("Moderate Health Status")
    else:
        st.error("Health Needs Attention")

    st.divider()

    st.subheader("📊 Health Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Health Score",
            f"{health_score}/100"
    )

    with col2:
        st.metric(
            "Risk %",
            f"{risk_percent:.1f}%"
    )

    with col3:
        st.metric(
            "BMI",
            bmi
    )

    with col4:
        st.metric(
            "Age",
            age
    )
    st.subheader("🎯 Current Risk Status")

    if risk_percent < 30:
        st.success("🟢 Low Risk")
    elif risk_percent < 70:
        st.warning("🟡 Moderate Risk")
    else:
        st.error("🔴 High Risk")

    st.subheader("🩺 Health Indicators")

    col1, col2 = st.columns(2)

    with col1:
        st.info(f"Glucose Level: {glucose}")

    with col2:
        st.info(f"Blood Pressure: {blood_pressure}")

    col3, col4 = st.columns(2)

    with col3:
        st.info(f"BMI: {bmi}")

    with col4:
        st.info(f"Insulin Level: {insulin}")

    st.subheader("🩺 Health Indicators")

    if glucose > 140:
        st.error(f"Glucose: {glucose} (High)")
    else:
        st.success(f"Glucose: {glucose} (Normal)")

    if bmi > 25:
        st.warning(f"BMI: {bmi} (Above Normal)")
    else:
        st.success(f"BMI: {bmi} (Healthy)")

    if risk_percent < 30:
        risk_level = "Low Risk"
    elif risk_percent < 70:
        risk_level = "Moderate Risk"
    else:
        risk_level = "High Risk"

    recommendations = []

    if glucose > 140:
        recommendations.append(
        "Reduce sugar intake and monitor blood glucose regularly."
    )

    if bmi > 25:
        recommendations.append(
        "Maintain a healthy weight through diet and exercise."
    )

    generate_pdf(
    "diabetes_report.pdf",
    risk_percent,
    health_score,
    risk_level,
    recommendations
)
    with open(
    "diabetes_report.pdf",
    "rb"
)   as pdf_file:
        st.download_button(
        label="📥 Download Report",
        data=pdf_file,
        file_name="diabetes_report.pdf",
        mime="application/pdf"
    )
