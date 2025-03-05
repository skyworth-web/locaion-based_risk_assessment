from langchain.llms import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Store API Key securely

def analyze_risk_factors(lat, lng):
    """Uses LangChain & OpenAI to analyze geographic and infrastructure risks"""
    llm = OpenAI(api_key=OPENAI_API_KEY)

    prompt = f"""
    Conduct a risk assessment for a location with coordinates {lat}, {lng}.
    Evaluate the following:
    - Geographic risks (proximity to water bodies, forests, disaster zones)
    - Infrastructure risks (road connectivity, hazardous sites nearby)
    Assign a risk score (1-5) and explain each factor.
    """
    
    response = llm(prompt)
    return response