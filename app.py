import streamlit as st
import requests

st.title("Location Risk Assessment")

company_name = st.text_input("Company Name")
location = st.text_input("Location")

if st.button("Assess Risk"):
    response = requests.post(
        "http://127.0.0.1:8000/risk_assessment/",
        json={"company_name": company_name, "location": location}
    )
    
    if response.status_code == 200:
        data = response.json()
        st.image(data["map_image_link"], caption="Location Image")
        st.write("Risk Analysis:", data["risk_analysis"])
    else:
        st.error("Invalid request!")
