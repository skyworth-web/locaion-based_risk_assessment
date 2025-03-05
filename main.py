from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google_maps_service import get_location_image
from risk_analysis import analyze_risk_factors

app = FastAPI()

class RiskAssessmentRequest(BaseModel):
    company_name: str
    location: str

@app.post("/risk_assessment/")
def risk_assessment(request: RiskAssessmentRequest):
    location_data = get_location_image(request.location)
    if not location_data:
        raise HTTPException(status_code=400, detail="Invalid location")

    risk_analysis = analyze_risk_factors(location_data["lat"], location_data["lng"])
    
    return {
        "company_name": request.company_name,
        "location": request.location,
        "map_image_link": location_data["image_url"],
        "risk_analysis": risk_analysis
    }

# Run with: uvicorn main:app --reload
