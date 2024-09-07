"""
planet_data.py

Contains data and constants for the planetary simulation,
including real values for planetary radii, distances, 
and other physical properties.

Author: Gierado Pham
Date: 2024-08-16
"""

# Import NASA API Planet Data Module
import NASA_API_Planet_Data

# Run NASA API Planet Data script to obtain planet data from NASA Horizon API
NASA_API_Planet_Data
#exec(open('NASA_API_Planet_Data.py').read())
print('Sucessfully Extracted Data from NASA Horizon')

# Astronimical Units (AU) is the average measured distance from planet Earth to the Sun
AU = 149e9    # in kilometers   

# Gravitational constant or attraction force between two bodies
G = 6.6743e-11    # in Newtons * m^2/kg^2      

# Sun Data
SUN = {
    #'radius':696340,    # in kilometers
    #'mass': 1.98892e30,    # in kilometers
    'radius':NASA_API_Planet_Data.df.iloc[0]['Radius (km)'],    # in kilometers
    'mass': NASA_API_Planet_Data.df.iloc[0]['Mass (kg)'],    # in kilometers
    'color': (255,255,0),   # color in simulation
    'orbital_distance': None,    # Orbital distance from the Sun
    'orbital_velocity': 0,    # Orbital velocity around the Sun
}

# Planet Data
MERCURY = {
    #'radius': 2439.7,    # in kilometers
    #'mass': 3.30e23,    # in kilograms
    'radius':NASA_API_Planet_Data.df.iloc[1]['Radius (km)'],    # in kilometers
    'mass': NASA_API_Planet_Data.df.iloc[1]['Mass (kg)'],    # in kilometers
    'color': (216, 103, 61),    # color in simulation
    'orbital_distance': 0.387 * AU,    # Orbital distance from the Sun
    'orbital_velocity': -47.9 * 1e3,    # Orbital velocity around the Sun
}

VENUS = {
    #'radius': 6051.8,    # in kilometers
    #'mass': 4.867e24,    # in kilograms
    'radius':NASA_API_Planet_Data.df.iloc[2]['Radius (km)'],    # in kilometers
    'mass': NASA_API_Planet_Data.df.iloc[2]['Mass (kg)'],    # in kilometers
    'color': (206, 174, 81),    # color in simulation
    'orbital_distance': 0.723 * AU,    # Orbital distance from the Sun
    'orbital_velocity': -35.0 * 1e3,    # Orbital velocity around the Sun
}

EARTH = {
    #'radius': 6371,    # in kilometers
    #'mass': 5.972e24,    # in kilograms
    'radius':NASA_API_Planet_Data.df.iloc[3]['Radius (km)'],    # in kilometers
    'mass': NASA_API_Planet_Data.df.iloc[3]['Mass (kg)'],    # in kilometers
    'color': (100, 149, 237),  # color in simulation
    'orbital_distance': 1.0 * AU,    # Orbital distance from the Sun
    'orbital_velocity': 29.8 * 1e3,    # Orbital velocity around the Sun
}

MARS = {
    #'radius': 3389.5,    # in kilometers
    #'mass': 6.4171e23,    # in kilograms
    'radius':NASA_API_Planet_Data.df.iloc[4]['Radius (km)'],    # in kilometers
    'mass': NASA_API_Planet_Data.df.iloc[4]['Mass (kg)'],    # in kilometers
    'color': (188, 39, 50),    # color in simulation
    'orbital_distance': 1.524 * AU,    # Orbital distance from the Sun
    'orbital_velocity': 24.1 * 1e3,    # Orbital velocity around the Sun
}

JUPITER = {
    #'radius': 69911,    # in kilometers
    #'mass': 1.898e27,    # in kilograms
    'radius':NASA_API_Planet_Data.df.iloc[5]['Radius (km)'],    # in kilometers
    'mass': NASA_API_Planet_Data.df.iloc[5]['Mass (kg)']/1000,    # in kilometers
    'color': (168, 106, 25),    # color in simulation
    'orbital_distance': 5.203 * AU,    # Orbital distance from the Sun
    'orbital_velocity': 20.05 * 1e3,    # Orbital velocity around the Sun
}

SATURN = {
    #'radius': 58232,    # in kilometers
    #'mass': 5.683e26,    # in kilograms
    'radius':NASA_API_Planet_Data.df.iloc[6]['Radius (km)'],    # in kilometers
    'mass': NASA_API_Planet_Data.df.iloc[6]['Mass (kg)'],    # in kilometers
    'color': (230, 171, 30),    # color in simulation
    'orbital_distance': 9.537 * AU,    # Orbital distance from the Sun
    'orbital_velocity': -18.46 * 1e3,    # Orbital velocity around the Sun
}

URANUS = {
    #'radius': 25362,    # in kilometers
    #'mass': 8.681e25,    # in kilograms
    'radius':NASA_API_Planet_Data.df.iloc[7]['Radius (km)'],    # in kilometers
    'mass': NASA_API_Planet_Data.df.iloc[7]['Mass (kg)'],    # in kilometers
    'color': (32, 230, 204),    # color in simulation
    'orbital_distance': 19.191 * AU,    # Orbital distance from the Sun
    'orbital_velocity': 18.11 * 1e3,    # Orbital velocity around the Sun
}

NEPTUNE = {
    #'radius': 24622,    # in kilometers
    #'mass': 1.024e26,    # in kilograms
    'radius':NASA_API_Planet_Data.df.iloc[8]['Radius (km)'],    # in kilometers
    'mass': NASA_API_Planet_Data.df.iloc[8]['Mass (kg)'],    # in kilometers
    'color': (14, 140, 225),    # color in simulation
    'orbital_distance': 30.069 * AU,    # Orbital distance from the Sun
    'orbital_velocity': -17.43 * 1e3,    # Orbital velocity around the Sun
}