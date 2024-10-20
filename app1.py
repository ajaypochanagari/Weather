import pandas as pd
import streamlit as st
import folium
from streamlit_folium import folium_static

df = pd.read_csv("meteo_top_20_villes_fr.csv")

cities = sorted(df["ville"].unique())

st.title("Informations météorologiques des 20 plus grandes villes de France")

# Mise en page à deux colonnes
col1, col2 = st.columns(2)

with col1:
    cities = [""] + sorted(df["ville"].unique())
    selected_city = st.selectbox("Sélectionnez une ville :", cities)

    if selected_city:

        city_df = df[df["ville"] == selected_city].reset_index(drop=True)
        st.write(f"**Ville :** {city_df['ville'][0]}")
        st.write(f"**Température actuelle :** {city_df['temperature'][0]}°C")
        st.write(f"**Température ressentie :** {city_df['temperature_res'][0]}°C")
        st.write(f"**Température minimale :** {city_df['temperature_min'][0]}°C")
        st.write(f"**Température maximale :** {city_df['temperature_max'][0]}°C")
        st.write(f"**Pression atmosphérique :** {city_df['pression'][0]} hPa")
        st.write(f"**Humidité :** {city_df['humidite'][0]}%")
        st.write(f"**Vitesse du vent :** {city_df['vent_vitesse'][0]} km/h")
        st.write(f"**Direction du vent :** {city_df['vent_direction'][0]}")
        st.write(f"**Lever du soleil :** {city_df['lever_soleil'][0]}")
        st.write(f"**Coucher du soleil :** {city_df['coucher_soleil'][0]}")


with col2:
    # Création de la carte de France avec des marqueurs pour chaque ville
    france_map = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

    for i, row in df.iterrows():
        ville = row["ville"]
        temperature = row["temperature"]
        lat = row["latitude"]
        lon = row["longitude"]

        # Création du marqueur pour la ville
        marker = folium.Marker(location=[lat, lon], tooltip=f"{ville} : {temperature}°C")

        # Ajout du marqueur à la carte
        marker.add_to(france_map)

    # Affichage de la carte dans l'interface utilisateur
    folium_static(france_map)
