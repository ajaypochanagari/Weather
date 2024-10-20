# Weather
Weather API Project
This project aims to manipulate APIs and retrieve data online. Using the Requests library, it is a question of interacting with the OpenWeatherMap API to retrieve and analyze the weather data of the 20 largest cities in France.
The information is stored in a pandas DataFrame and exported to a CSV file. We are also creating an SQLite database.

The coord_villes.ipynb notebook uses a geocoding API to add the latitude and longitude columns to the previously created DataFrame.

The app1.py file contains a Streamlit application to display the weather information of the 20 cities. It allows you to select a city from a drop-down list and displays the weather information for that city. The page also includes a map of France with markers for each city.

The app2.py file contains another Streamlit application that allows the user to enter the name of a city and view the weather information for that city. The page also includes a world map with markers for all 20 cities.

Installation
To run this project, you will need the following libraries:

* Pandas  
* Streamlit  
* Folium  
* Streamlit-folium  
* Requests  
* Dotenv  
You can install them with the following command:

pip install pandas streamlit folium streamlit-folium requests python-dotenv

You will also need an API key to access the OpenWeatherMap API. This key must be stored in an .env file at the root of the project.

Usage
To run the application, run the following command at the root of the project:

Streamlit Run app1.py or Streamlit Run app2.py

This will open the app in your default browser.
