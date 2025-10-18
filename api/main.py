from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import requests
from datetime import datetime, timezone



app = FastAPI()

CATFACT_URL = "https://catfact.ninja/fact"

# Load user info from environment or directly define

@app.get("/me")
def get_profile():
    try:
        # Fetch random cat fact
        response = requests.get(CATFACT_URL, timeout=5)
        response.raise_for_status()
        fact_data = response.json()
        cat_fact = fact_data.get("fact", "Cats are mysterious creatures 😺")

    except requests.RequestException:
        cat_fact = "Could not fetch a cat fact at this moment. Try again later."

    # Current UTC time in ISO 8601 format
    current_time = datetime.now(timezone.utc).isoformat()

    payload = {
        "status": "success",
        "user": {
            "email": "balogunafebu22@gmail.com",
            "name": "Balogun Afebu",
            "stack": "Python/FastAPI",
        },
        "timestamp": current_time,
        "fact": cat_fact
    }

    return JSONResponse(content=payload, media_type="application/json")
