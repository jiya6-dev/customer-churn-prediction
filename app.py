import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# =========================
# LOAD MODEL + DATA
# =========================
model = model = joblib.load("rf_model_small.pkl")
model_columns = joblib.load("model_columns.pkl")

df = pd.read_csv("European_Bank.csv")

# =========================
# CLEAN DATA
# =========================
df = df.drop(columns=["Year"], errors="ignore")

df["Balance_Salary_Ratio"] = df["Balance"] / (df["EstimatedSalary"] + 1)
df["Product_Density"] = df["NumOfProducts"] / (df["Tenure"] + 1)
df["Age_Tenure_Interaction"] = df["Age"] * df["Tenure"]

for col in ["Geography_Germany", "Geography_Spain", "Gender_Male"]:
    if col in df.columns:
        df[col] = df[col].astype(int)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Churn Dashboard", layout="wide")
st.title("🏦 Customer Churn Analytics Dashboard")

# =========================
# SESSION STATE
# =========================
if "prob" not in st.session_state:
    st.session_state.prob = None
if "pred" not in st.session_state:
    st.session_state.pred = None

# =========================
# SIDEBAR INPUTS
# =========================
st.sidebar.header("Customer Input")

credit_score = st.sidebar.slider("Credit Score", 300, 900, 650)
age = st.sidebar.slider("Age", 18, 100, 35)
tenure = st.sidebar.slider("Tenure", 0, 10, 3)
balance = st.sidebar.number_input("Balance", 0.0, 250000.0, 50000.0)
num_products = st.sidebar.slider("Products", 1, 4, 1)
has_cr_card = st.sidebar.selectbox("Credit Card", [0, 1])
is_active = st.sidebar.selectbox("Active Member", [0, 1])
salary = st.sidebar.number_input("Salary", 0.0, 200000.0, 50000.0)

geography = st.sidebar.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

# =========================
# FILTERS
# =========================
st.sidebar.header("Filters")

age_range = st.sidebar.slider("Age Range", 18, 100, (25, 50))
balance_range = st.sidebar.slider("Balance Range", 0, 250000, (0, 100000))

filtered_df = df[
    (df["Age"].between(age_range[0], age_range[1])) &
    (df["Balance"].between(balance_range[0], balance_range[1]))
]

# =========================
# FEATURE ENGINEERING
# =========================
balance_salary_ratio = balance / (salary + 1)
product_density = num_products / (tenure + 1)
age_tenure_interaction = age * tenure

input_data = {
    "CreditScore": credit_score,
    "Age": age,
    "Tenure": tenure,
    "Balance": balance,
    "NumOfProducts": num_products,
    "HasCrCard": has_cr_card,
    "IsActiveMember": is_active,
    "EstimatedSalary": salary,
    "Balance_Salary_Ratio": balance_salary_ratio,
    "Product_Density": product_density,
    "Age_Tenure_Interaction": age_tenure_interaction,
    "Geography_Germany": 1 if geography == "Germany" else 0,
    "Geography_Spain": 1 if geography == "Spain" else 0,
    "Gender_Male": 1 if gender == "Male" else 0
}

input_df = pd.DataFrame([input_data])
input_df = input_df.reindex(columns=model_columns, fill_value=0)

# =========================
# PREDICTION FUNCTION
# =========================
def predict():
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]
    return pred, prob

# =========================
# PREDICTION UI
# =========================
if st.button("🔍 Predict Churn"):

    pred, prob = predict()

    st.session_state.pred = pred
    st.session_state.prob = prob

# =========================
# DISPLAY RESULT (SAFE)
# =========================
if st.session_state.prob is not None:

    prob = st.session_state.prob
    pred = st.session_state.pred

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Churn Probability", f"{prob:.2%}")
    col2.metric("Prediction", "CHURN" if pred == 1 else "RETAIN")
    col3.metric("Risk Level",
                "HIGH" if prob > 0.7 else "MEDIUM" if prob > 0.3 else "LOW")
    col4.metric("Confidence", f"{max(prob, 1-prob):.2%}")

    st.divider()

    # =========================
    # RISK SEGMENTS
    # =========================
    st.subheader("🎯 Risk Segment")

    if prob < 0.3:
        st.success("🟢 Low Risk Customer")
    elif prob < 0.7:
        st.warning("🟡 Medium Risk Customer")
    else:
        st.error("🔴 High Risk Customer")

    # =========================
    # GAUGE
    # =========================
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Churn Risk Score"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red" if prob > 0.7 else "orange" if prob > 0.3 else "green"},
            'steps': [
                {'range': [0, 30], 'color': "lightgreen"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "salmon"}
            ]
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

# =========================
# BUSINESS DASHBOARD
# =========================
st.header("📊 Business Intelligence Dashboard")

# Age vs churn
fig_age = px.histogram(
    filtered_df,
    x="Age",
    color="Exited",
    barmode="overlay",
    title="Age vs Churn"
)
st.plotly_chart(fig_age, use_container_width=True)

# Balance vs churn
fig_balance = px.box(
    filtered_df,
    x="Exited",
    y="Balance",
    color="Exited",
    title="Balance vs Churn"
)
st.plotly_chart(fig_balance, use_container_width=True)

# Salary vs churn
fig_salary = px.box(
    filtered_df,
    x="Exited",
    y="EstimatedSalary",
    color="Exited",
    title="Salary vs Churn"
)
st.plotly_chart(fig_salary, use_container_width=True)

# Products vs churn
prod_churn = df.groupby("NumOfProducts")["Exited"].mean().reset_index()

fig_prod = px.line(
    prod_churn,
    x="NumOfProducts",
    y="Exited",
    markers=True,
    title="Products vs Churn"
)
st.plotly_chart(fig_prod, use_container_width=True)

# Geography
geo_churn = df.groupby("Geography")["Exited"].mean().reset_index()

fig_geo = px.bar(
    geo_churn,
    x="Geography",
    y="Exited",
    title="Geography vs Churn"
)
st.plotly_chart(fig_geo, use_container_width=True)

# =========================
# INSIGHTS
# =========================
st.subheader("🧠 Business Insights")

insights = []

if df["Age"].mean() > 40:
    insights.append("Older customers show higher churn risk.")

if df["Balance"].mean() > df["Balance"].median():
    insights.append("High balance customers are sensitive to churn.")

if df["NumOfProducts"].mean() < 2:
    insights.append("Low product usage increases churn risk.")

if df["IsActiveMember"].mean() < 0.5:
    insights.append("Low engagement drives churn.")

for i in insights:
    st.info(i)

# =========================
# FEATURE IMPORTANCE
# =========================
st.subheader("🔍 Feature Importance")

importances = model.feature_importances_

feat_df = pd.DataFrame({
    "Feature": model_columns,
    "Importance": importances
}).sort_values("Importance", ascending=False).head(10)

fig_imp = px.bar(
    feat_df,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Top Drivers of Churn"
)

st.plotly_chart(fig_imp, use_container_width=True)
