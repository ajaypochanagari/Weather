import os
from os.path import join, dirname
from dotenv import load_dotenv
import streamlit as st
import requests
from openweather import show_weather_data
import folium
from streamlit_folium import folium_static


dotenv_path = join(dirname("DECOUVERTE_REQUESTS"), '.env')
load_dotenv(dotenv_path)
API_KEY = os.environ.get("API_KEY")


st.title("Informations météorologiques")
col1, col2 = st.columns(2)

with col1:
       
    city = st.text_input("Entrez le nom de la ville:")
    if city:
        show_weather_data(city)


villes = ["Paris", "Marseille", "Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Montpellier", "Bordeaux", "Lille", "Rennes", 
          "Reims", "Le Havre", "Saint-Étienne", "Toulon", "Grenoble", "Dijon", "Angers", "Nîmes", "Villeurbanne"]

with col2:
    # Création de la carte centrée sur le monde entier
    france_map = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

    # Boucle sur les villes pour récupérer les coordonnées géographiques et ajouter les marqueurs à la carte
    for ville in villes:
        # Requête vers l'API Geocoding de OpenWeatherMap
        url = f"http://api.openweathermap.org/geo/1.0/direct?q={ville}&limit=1&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()

        # Obtention des données météorologiques pour la ville
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric'
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        temperature = weather_data["main"]["temp"]
        
        # Création du marqueur pour la ville
        marker = folium.Marker(location=[lat, lon], tooltip=f"{ville} : {temperature}°C")

        # Ajout du marqueur à la carte
        marker.add_to(france_map)

    # Affichage de la carte dans l'interface utilisateur
    folium_static(france_map)
 
