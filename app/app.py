
import streamlit as st
import pandas as pd
import joblib

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="MediBuddy Insurance Dashboard",
    page_icon="🏥",
    layout="wide"
)

# ==========================================
# 2. LOAD MODEL
# ==========================================

@st.cache_resource
def load_model():
    return joblib.load("medibuddy_best_model.pkl")

try:
    model = load_model()
except Exception as e:
    st.error(f"Model loading error: {e}")
    st.stop()

# ==========================================
# 3. CUSTOM CSS
# ==========================================

st.markdown("""
<style>
.main-title {
    font-size: 35px;
    font-weight: bold;
    color: #1976D2;
}

.subtitle {
    font-size: 16px;
    color: gray;
}

div.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. TOP NAVIGATION
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

st.title("🏥 MediBuddy")

st.caption("Medical Insurance Charges Prediction System")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"

with col2:
    if st.button("💰 Prediction", use_container_width=True):
        st.session_state.page = "Insurance Prediction"

with col3:
    if st.button("📊 About Project", use_container_width=True):
        st.session_state.page = "About Project"

with col4:
    if st.button("🏢 About Company", use_container_width=True):
        st.session_state.page = "About Company"

st.divider()

page = st.session_state.page

# ==========================================
# 5. DASHBOARD PAGE
# ==========================================

if page == "Dashboard":

    st.markdown(
        '<p class="main-title">MediBuddy Dashboard</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Medical Insurance Charges Prediction System</p>',
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    col1.metric("Dataset Records", "1,338")
    col2.metric("ML Model", "Gradient Boosting")
    col3.metric("Model R² Score", "86.54%")

    st.divider()

    st.subheader("Project Overview")

    st.write("""
    MediBuddy is a Machine Learning application that estimates
    medical insurance charges based on customer information.

    The model uses features such as:

    - Age
    - Gender
    - BMI
    - Number of children
    - Smoking status
    - Geographical region
    """)

    st.success(
        "Navigate to Prediction to estimate customer insurance charges."
    )

# ==========================================
# 6. INSURANCE PREDICTION PAGE
# ==========================================

elif page == "Insurance Prediction":

    st.title("💰 Insurance Charges Prediction")

    st.write(
        "Enter customer information to estimate insurance charges."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=30
        )

        bmi = st.number_input(
            "BMI",
            min_value=10.0,
            max_value=60.0,
            value=27.5
        )

        children = st.number_input(
            "Number of Children",
            min_value=0,
            max_value=10,
            value=0
        )

    with col2:

        sex = st.selectbox(
            "Gender",
            ["Female", "Male"]
        )

        smoker = st.selectbox(
            "Smoking Status",
            ["No", "Yes"]
        )

        region = st.selectbox(
            "Region",
            ["Northeast", "Northwest", "Southeast", "Southwest"]
        )

    st.divider()

    if st.button("Predict Insurance Charges", type="primary"):

        input_data = pd.DataFrame({
            "children": [children],
            "age": [age],
            "bmi": [bmi],
            "sex_male": [1 if sex == "Male" else 0],
            "smoker_yes": [1 if smoker == "Yes" else 0],
            "region_northwest": [1 if region == "Northwest" else 0],
            "region_southeast": [1 if region == "Southeast" else 0],
            "region_southwest": [1 if region == "Southwest" else 0]
        })

        feature_columns = [
            "children",
            "age",
            "bmi",
            "sex_male",
            "smoker_yes",
            "region_northwest",
            "region_southeast",
            "region_southwest"
        ]

        input_data = input_data[feature_columns]

        try:

            prediction = model.predict(input_data)[0]

            st.success("Prediction completed successfully!")

            st.metric(
                "Estimated Insurance Charges",
                f"₹ {prediction:,.2f}"
            )

            st.caption(
                "This is a model-generated estimate, not an actual quotation."
            )

        except Exception as e:

            st.error(f"Prediction failed: {e}")

# ==========================================
# 7. ABOUT PROJECT PAGE
# ==========================================

elif page == "About Project":

    st.title("📊 About the Project")

    st.subheader("Medical Insurance Charges Prediction")

    st.write("""
    **Project Objective**

    The objective of this project is to analyze customer health
    and demographic information and predict medical insurance
    charges using Machine Learning.

    **Input Features**

    - Age
    - Gender
    - BMI
    - Number of children
    - Smoking status
    - Geographical region

    **Target Variable**

    - Medical Insurance Charges in INR

    **Machine Learning Algorithm**

    - Gradient Boosting Regressor

    **Technology Stack**

    - Python
    - Pandas
    - NumPy
    - Matplotlib
    - Seaborn
    - Scikit-learn
    - Streamlit
    - Joblib
    """)

    st.divider()

    st.subheader("Model Performance")

    col1, col2, col3 = st.columns(3)

    col1.metric("MAE", "₹2,352.75")
    col2.metric("RMSE", "₹4,377.71")
    col3.metric("R² Score", "86.54%")

    st.info(
        "The original Gradient Boosting model was selected "
        "because it performed better than its tuned version "
        "on the test dataset."
    )

# ==========================================
# 8. ABOUT COMPANY PAGE
# ==========================================

elif page == "About Company":

    st.title("🏢 About MediBuddy")

    st.subheader("Company Overview")

    st.write("""
    MediBuddy is a digital healthcare platform that provides
    healthcare services and benefits to individuals and
    organizations.

    The platform focuses on three major service areas:
    """)

    # Company Services

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🏥 Inpatient Care")
        st.write("""
        Healthcare services related to hospitalization
        and inpatient medical treatment.
        """)

    with col2:
        st.subheader("🩺 Outpatient Services")
        st.write("""
        Healthcare services that allow people to access
        medical care without hospital admission.
        """)

    with col3:
        st.subheader("💼 Corporate Wellness")
        st.write("""
        Healthcare and wellness benefits designed
        for corporate employees and organizations.
        """)

    st.divider()

    st.subheader("About the Organization")

    st.write("""
    MediBuddy is the technology platform from Medi Assist.

    It aims to transform the health insurance industry by
    making the process of discovering, accessing, utilizing,
    and monitoring health benefits seamless, real-time,
    and virtually paperless.
    """)

    st.divider()

    st.subheader("Company Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Founded Year", "2000")

    with col2:
        st.metric("Headquarters", "Bengaluru, India")

    st.write("""
    **Company Name:** MediBuddy

    **Parent Organization / Platform Association:** Medi Assist

    **Industry:** Digital Healthcare and Health Insurance Technology

    **Headquarters:** Bengaluru, Karnataka, India
    """)

    st.divider()

    st.subheader("Company Mission")

    st.write("""
    To simplify healthcare access and health benefits through
    technology, helping individuals and organizations discover,
    access, utilize, and monitor healthcare services more easily.
    """)

    st.caption(
        "Company information based on the MediBuddy Capstone Project assignment."
    )

# ==========================================
# 9. FOOTER
# ==========================================

st.divider()

st.caption(
    "MediBuddy | Medical Insurance Charges Prediction | "
    "Machine Learning Project"
)
