from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "Weather API works!"
    }


@app.get("/weather/{city}")
def get_weather(city: str):

    url = (
        f"https://wttr.in/{city}?format=j1"
    )

    response = requests.get(url)

    data = response.json()

    current = data["current_condition"][0]

    return {

        "city": city,

        "temperature":
        current["temp_C"],

        "description":
        current["weatherDesc"][0]["value"],

        "humidity":
        current["humidity"]
    }