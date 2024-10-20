
import os
from os.path import join, dirname
from dotenv import load_dotenv
import streamlit as st
import requests
from datetime import datetime


dotenv_path = join(dirname("DECOUVERTE_REQUESTS"), '.env')
load_dotenv(dotenv_path)
API_KEY = os.environ.get("API_KEY")

api_key = API_KEY

def get_weather_data(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    temperature = data["main"]["temp"]
    temperature_res = data["main"]["feels_like"]
    temperature_min = data["main"]["temp_min"]
    temperature_max = data["main"]["temp_max"]
    pression = data["main"]["pressure"]
    humidite = data["main"]["humidity"]
    vent_vitesse = data["wind"]["speed"]
    vent_direction = data["wind"]["deg"]
    lever_soleil_timestamp = data["sys"]["sunrise"]
    coucher_soleil_timestamp = data["sys"]["sunset"]

    lever_soleil = datetime.fromtimestamp(lever_soleil_timestamp).strftime("%H:%M:%S")
    coucher_soleil = datetime.fromtimestamp(coucher_soleil_timestamp).strftime("%H:%M:%S")
    
    weather_data = {
                "temperature": temperature,
                "temperature_res": temperature_res,
                "temperature_min": temperature_min,
                "temperature_max": temperature_max,
                "pression": pression,
                "humidite": humidite,
                "vent_vitesse": vent_vitesse,
                "vent_direction": vent_direction,
                "lever_soleil": lever_soleil,
                "coucher_soleil": coucher_soleil}
    return weather_data


def show_weather_data(city):
        data = get_weather_data(city)
        st.write(f"**Température** : {data['temperature']} °C")
        st.write(f"**Température ressentie** : {data['temperature_res']} °C")
        st.write(f"**Température minimale** : {data['temperature_min']} °C")
        st.write(f"**Température maximale** : {data['temperature_max']} °C")
        st.write(f"**Pression atmosphérique** : {data['pression']} hPa")
        st.write(f"**Humidité** : {data['humidite']} %")
        st.write(f"**Vitesse du vent** : {data['vent_vitesse']} km/h")
        st.write(f"**Direction du vent** : {data['vent_direction']}°")
        st.write(f"**Lever du soleil** : {data['lever_soleil']} ")
        st.write(f"**Coucher du soleil** : {data['coucher_soleil']} ")
        
