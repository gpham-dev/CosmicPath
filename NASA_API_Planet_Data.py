"""
NASA_API_Planet_Data.py

Contains data and constants for the planetary simulation,
including real values for planetary radii, distances, 
and other physical properties.

Author: Gierado Pham
Date: 2024-09-05
"""
import requests
import re
import pandas as pd

# NASA HORIZONS API URL
url = "https://ssd.jpl.nasa.gov/api/horizons.api"

# Dictionary for each planet and their respective IDs in NASA Horizon
planet_dict = {
    "Sun":"10",  # The sun is a celestial body but we will put it here for now
    "Mercury": "199",
    "Venus": "299",
    "Earth": "399",
    "Mars": "499",
    "Jupiter": "599",
    "Saturn": "699",
    "Uranus": "799",
    "Neptune": "899"
}

# Initialize list to store planet data
planet_data = []

# Function to fetch NASA Horizon API to obtain planet data
def fetch_planet_data(planet_name, planet_id):
    params = {
        "format": "json",
        "COMMAND": planet_id,
        "OBJ_DATA": "YES",
        "MAKE_EPHEM": "NO",
    }

    # Send the request to NASA HORIZONS
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        print(f"Error fetching data for {planet_name}: Status code {response.status_code}")
        return

    # Parse the JSON response
    data = response.json()
    result_text = data.get('result', '')

    # Print result text for debugging
    #print(f"Result text for {planet_name}: {result_text}")

    # Use regex to parse mass, radius, distance from Sun, and orbital velocity
    mass = re.search(r"Mass x10\^(\d+) \(kg\)\s*=\s*([\d\.]+)", result_text)
    radius = re.search(r"Vol\. Mean Radius \(km\)\s*=\s*([\d\.]+)", result_text)
    distance = re.search(r"Mean distance from Sun \(km\)\s*=\s*([\d\.]+)", result_text)
    orbital_velocity = re.search(r"Mean Orbit vel.\  km/s\s*=\s*([\d\.]+)", result_text)
    
    # Accounting for different mass, radius, and orbital velocity outputs for each planet
    if not mass:
        mass = re.search(r"Mass x 10\^(\d+) \(g\)\s*=\s*([\d\.]+)", result_text)
        if not mass:
            mass = re.search(r"Mass, 10\^(\d+) kg\s*=\s~*([\d\.]+)", result_text)

    if not radius:
        radius = re.search(r"Vol\. mean radius \(km\)\s*=\s*([\d\.]+)", result_text)
        if not radius:
            radius = re.search(r"Vol\. mean radius, km\s*=\s*([\d\.]+)", result_text)
    if not orbital_velocity:
        orbital_velocity = re.search(r"Orbit speed,\ km/s\s*=\s*([\d\.]+)", result_text)
        if not orbital_velocity:
            orbital_velocity = re.search(r"Orbital speed,\ km/s\s*=\s*([\d\.]+)", result_text)
            if not orbital_velocity:
                orbital_velocity = re.search(r"Mean orbit speed,\ km/s\s*=\s*([\d\.]+)", result_text)
                if not orbital_velocity:
                    orbital_velocity = re.search(r"Mean orbit velocity \s*=\s*([\d\.]+)", result_text)
                    if not orbital_velocity:
                        orbital_velocity = re.search(r"Orbital speed,\  km/s\s*=\s*([\d\.]+)", result_text)


    # Mass
    if mass:
        power_factor = int(mass.group(1))
        mass_value = float(mass.group(2))
        mass = mass_value * (10 ** power_factor)
    else:
        mass = None
        print(f"Mass data not found for {planet_name}")

    # Radius
    if radius:
        radius = float(radius.group(1))
    else:
        radius = None
        print(f"Radius data not found for {planet_name}")

    # Distance from Sun
    # if distance:
    #     distance = float(distance.group(1))
    # else:
    #     distance = None
    #     print(f"Distance data not found for {planet_name}")

    # Orbital Velocity
    if orbital_velocity:
        orbital_velocity = float(orbital_velocity.group(1))
    else:
        orbital_velocity = None
        print(f"Orbital velocity data not found for {planet_name}")

    # Append fetched data to planet_data list
    planet_data.append({
        "Planet": planet_name,
        "Radius (km)": radius,
        "Mass (kg)": mass,
        "Distance to Sun (km)": distance,
        "Orbital Velocity (km/s)": orbital_velocity
    })

print("Fetching Data")
for planet_name, planet_id in planet_dict.items():
    fetch_planet_data(planet_name, planet_id)
print("Fetching Data Completed")

# Convert list to DataFrame and print
df = pd.DataFrame(planet_data)
print("Results Summary: ")
print(df)