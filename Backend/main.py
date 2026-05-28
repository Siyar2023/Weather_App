# Import FastAPI framework for building APIs
from fastapi import FastAPI

# Import CORS middleware to allow frontend (browser) to communicate with backend
from fastapi.middleware.cors import CORSMiddleware

# Import requests library to make HTTP requests to external APIs
import requests


# Create FastAPI app instance
app = FastAPI()


# Add CORS middleware
# This allows your frontend (HTML/JS) to call this API even if it's on another port (e.g. 5500, 3000)
app.add_middleware(
    CORSMiddleware,

    # Allow all origins (NOT safe for production, but OK for learning/projects)
    allow_origins=["*"],

    # Allow cookies / authentication headers
    allow_credentials=True,

    # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_methods=["*"],

    # Allow all headers from frontend requests
    allow_headers=["*"],
)


# Root endpoint (test route)
@app.get("/")
def home():
    # Returns a simple JSON response to confirm API is running
    return {
        "message": "Weather API works!"
    }


# Dynamic route that takes a city name from the URL
@app.get("/weather/{city}")
def get_weather(city: str):

    # Build URL for external weather API (wttr.in)
    # {city} is inserted into the URL dynamically
    url = (
        f"https://wttr.in/{city}?format=j1"
    )

    # Send HTTP GET request to the weather API
    response = requests.get(url)

    # Convert API response from JSON string into Python dictionary
    data = response.json()

    # Extract current weather data from the response
    current = data["current_condition"][0]

    # Return only the important data to the frontend
    return {

        # City name from the URL parameter
        "city": city,

        # Temperature in Celsius
        "temperature":
        current["temp_C"],

        # Weather description (e.g. Sunny, Cloudy, Rainy)
        "description":
        current["weatherDesc"][0]["value"],

        # Humidity percentage
        "humidity":
        current["humidity"]
    }


# ========================================================
# WEATHER API (FASTAPI) - HOW IT WORKS (STEP BY STEP)
# ========================================================

# 1. FastAPI application is created
# app = FastAPI()

# 2. CORS middleware allows frontend to talk to backend
# Without this, browser will block requests

# 3. "/" route is a test endpoint
# Returns simple message to confirm API is running

# 4. "/weather/{city}" is dynamic route
# It takes city name from URL (example: /weather/Bangkok)

# 5. Backend builds external API URL:
# https://wttr.in/{city}?format=j1

# 6. Sends request to weather API using requests.get()

# 7. Converts response into Python dictionary (JSON)

# 8. Extracts current weather data

# 9. Returns only needed data:
# - city
# - temperature
# - description
# - humidity

# 10. Frontend receives this JSON and displays it dynamically

# ========================================================