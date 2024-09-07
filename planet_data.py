"""
planet_data.py

Contains data and constants for the planetary simulation,
including real values for planetary radii, distances, 
and other physical properties.

Author: Gierado Pham
Date: 2024-08-16

Planet Data:
- radius: Radius of the planet (in kilometers)
- mass: Mass of the planet (in kilograms)
- color: Color used in the simulation
- orbital_distance: Distance from the Sun (in Astronomical Units)
- orbital_velocity: Orbital velocity around the Sun (in km/s)
"""

# Import NASA API Planet Data Module
import NASA_API_Planet_Data

# Run NASA API Planet Data script to obtain planet data from NASA Horizon API
NASA_API_Planet_Data
print('Sucessfully Extracted Data from NASA Horizon')

# Astronimical Units (AU) is the average measured distance from planet Earth to the Sun
AU = 149e9    # in kilometers   

# Gravitational constant or attraction force between two bodies
G = 6.6743e-11    # in Newtons * m^2/kg^2      

# Sun Data
SUN = {
    'radius':NASA_API_Planet_Data.df.iloc[0]['Radius (km)'],
    'mass': NASA_API_Planet_Data.df.iloc[0]['Mass (kg)'],  
    'color': (255,255,0),  
    'orbital_distance': None,    
    'orbital_velocity': 0,   
}

# Planet Data
MERCURY = {
    'radius':NASA_API_Planet_Data.df.iloc[1]['Radius (km)'],    
    'mass': NASA_API_Planet_Data.df.iloc[1]['Mass (kg)'],    
    'color': (216, 103, 61), 
    'orbital_distance': 0.387 * AU, 
    'orbital_velocity': NASA_API_Planet_Data.df.iloc[1]['Orbital Velocity (km/s)'] * -1 * 1e3  
}

VENUS = {
    'radius':NASA_API_Planet_Data.df.iloc[2]['Radius (km)'],  
    'mass': NASA_API_Planet_Data.df.iloc[2]['Mass (kg)'],   
    'color': (206, 174, 81),  
    'orbital_distance': 0.723 * AU,  
    'orbital_velocity': NASA_API_Planet_Data.df.iloc[2]['Orbital Velocity (km/s)'] * -1 * 1e3
}

EARTH = { 
    'radius':NASA_API_Planet_Data.df.iloc[3]['Radius (km)'],    
    'mass': NASA_API_Planet_Data.df.iloc[3]['Mass (kg)'],   
    'color': (100, 149, 237),  
    'orbital_distance': 1.0 * AU,    
    'orbital_velocity': NASA_API_Planet_Data.df.iloc[3]['Orbital Velocity (km/s)'] * -1 * 1e3
}

MARS = {
    'radius':NASA_API_Planet_Data.df.iloc[4]['Radius (km)'],  
    'mass': NASA_API_Planet_Data.df.iloc[4]['Mass (kg)'],   
    'color': (188, 39, 50),    
    'orbital_distance': 1.524 * AU,    
    'orbital_velocity': NASA_API_Planet_Data.df.iloc[4]['Orbital Velocity (km/s)'] * -1 * 1e3
}

JUPITER = {
    'radius':NASA_API_Planet_Data.df.iloc[5]['Radius (km)'],  
    'mass': NASA_API_Planet_Data.df.iloc[5]['Mass (kg)']/1000,   
    'color': (168, 106, 25),   
    'orbital_distance': 5.203/2.3 * AU,  
    'orbital_velocity': NASA_API_Planet_Data.df.iloc[5]['Orbital Velocity (km/s)'] * -1.53 * 1e3   
}

SATURN = {   
    'radius':NASA_API_Planet_Data.df.iloc[6]['Radius (km)'],    
    'mass': NASA_API_Planet_Data.df.iloc[6]['Mass (kg)'],   
    'color': (230, 171, 30),   
    'orbital_distance': 9.537/3.4 * AU,   
    'orbital_velocity': NASA_API_Planet_Data.df.iloc[6]['Orbital Velocity (km/s)'] * -1.91 * 1e3   
}

URANUS = {
    'radius':NASA_API_Planet_Data.df.iloc[7]['Radius (km)'],   
    'mass': NASA_API_Planet_Data.df.iloc[7]['Mass (kg)'],   
    'color': (32, 230, 204),   
    'orbital_distance': 19.191/5.7 * AU,  
    'orbital_velocity': NASA_API_Planet_Data.df.iloc[7]['Orbital Velocity (km/s)'] * -2.66 * 1e3  
}

NEPTUNE = {
    'radius':NASA_API_Planet_Data.df.iloc[8]['Radius (km)'], 
    'mass': NASA_API_Planet_Data.df.iloc[8]['Mass (kg)'],   
    'color': (14, 140, 225),   
    'orbital_distance': 30.069/7.8 * AU, 
    'orbital_velocity': NASA_API_Planet_Data.df.iloc[8]['Orbital Velocity (km/s)'] * -3.21 * 1e3 
}