"""
planet_data.py

Contains data and constants for the planetary simulation,
including real values for planetary radii, distances, 
and other physical properties.

Author: Gierado Pham
Date: 2024-08-16
"""

# Astronimical Units (AU) is the average measured distance from planet Earth to the Sun

AU = 149e6 # in kilometers

# Define a scale factor to scale down the orbital distances in order to fit all planets
# in the simulation window.

SCALE_FACTOR = 1/1e9    

# Sun Data
SUN = {
    'radius':696340,    # in kilometers
    'mass': 1.98892e30,    # in kilometers
    'color': (255,255,0),   # color in simulation
    'orbital_distance': None    # Orbital distance from the Sun
}

# Planet Data
MERCURY = {
    'radius': 2439.7,  # in kilometers
    'mass': 3.30e23,  # in kilograms
    'color': (216, 103, 61),  # color in simulation
    'orbital_distance': 0.387 * AU * SCALE_FACTOR # Orbital distance from the Sun
}

VENUS = {
    'radius': 6051.8,  # in kilometers
    'mass': 4.867e24,  # in kilograms
    'color': (206, 174, 81),  # color in simulation
    'orbital_distance': 0.723 * AU  * SCALE_FACTOR # Orbital distance from the Sun
}

EARTH = {
    'radius': 6371,  # in kilometers
    'mass': 5.972e24,  # in kilograms
    'color': (100, 149, 237),  # color in simulation
    'orbital_distance': 1.0 * AU * SCALE_FACTOR  # Orbital distance from the Sun
}

MARS = {
    'radius': 3389.5,  # in kilometers
    'mass': 6.4171e23,  # in kilograms
    'color': (188, 39, 50),  # color in simulation
    'orbital_distance': 1.524 * AU * SCALE_FACTOR  # Orbital distance from the Sun
}

JUPITER = {
    'radius': 69911,  # in kilometers
    'mass': 1.898e27,  # in kilograms
    'color': (168, 106, 25),  # color in simulation
    'orbital_distance': 5.203 * AU * SCALE_FACTOR  # Orbital distance from the Sun
}

SATURN = {
    'radius': 58232,  # in kilometers
    'mass': 5.683e26,  # in kilograms
    'color': (230, 171, 30),  # color in simulation
    'orbital_distance': 9.537 * AU * SCALE_FACTOR  # Orbital distance from the Sun
}

URANUS = {
    'radius': 25362,  # in kilometers
    'mass': 8.681e25,  # in kilograms
    'color': (32, 230, 204),  # color in simulation
    'orbital_distance': 19.191 * AU * SCALE_FACTOR  # Orbital distance from the Sun
}

NEPTUNE = {
    'radius': 24622,  # in kilometers
    'mass': 1.024e26,  # in kilograms
    'color': (14, 140, 225),  # color in simulation
    'orbital_distance': 30.069 * AU * SCALE_FACTOR  # Orbital distance from the Sun
}

