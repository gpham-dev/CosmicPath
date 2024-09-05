import requests
import re

# NASA HORIZONS API URL
url = "https://ssd.jpl.nasa.gov/api/horizons.api"

# Define the parameters for the request
params = {
    "format": "json",
    "COMMAND": "399",  # '399' is the ID for Earth in HORIZONS
    "OBJ_DATA": "YES",  # Get object data
    "MAKE_EPHEM": "NO",  # We don’t need ephemeris data here
}

# Send the request to NASA HORIZONS
response = requests.get(url, params=params)

# Parse the JSON response
if response.status_code == 200:
    data = response.json()
    print(response.text)
    # Extract the plain text result
    result_text = data.get('result', '')
    
    # Use regex to parse mass, radius, distance from Sun, and orbital velocity
    mass = re.search(r"Mass x10\^(\d+) \(kg\)= ([\d\.]+)", result_text)
    radius = re.search(r"Vol\. Mean Radius \(km\)\s+= ([\d\.]+)", result_text)
    distance = re.search(r"Mean distance from Sun \(km\)\s+= ([\d\.]+)", result_text)
    orbital_velocity = re.search(r"Orbital speed, km/s\s*=\s*([\d\.]+)", result_text)

    # Mass
    power_factor = int(mass.group(1))
    mass_value = float(mass.group(2))
    mass = mass_value * (10 ** power_factor)
    print(f"Mass: {mass} kg")

    # Radius
    radius = float(radius.group(1))
    print(f"Radius: {radius} km")

    # # Distance from Sun
    # distance_from_sun = float(distance.group(1))
    # print(f"Distance from Sun: {distance_from_sun} km")

    # Orbital Velocity
    orbital_velocity = float(orbital_velocity.group(1))
    print(f"Orbital Velocity: {orbital_velocity} km/s")


    print(mass)

