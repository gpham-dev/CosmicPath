"""
Planet_Simulation.py

Simulation of Planetary Motions with real values and physics.

Author: Gierado Pham
Date: 2024-08-16
"""

# Importing necessary modules
import pygame
import math
import planet_data
pygame.init()

WIDTH, HEIGHT = 1900, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

FONT = pygame.font.SysFont("comicsans", 16)

space_image = pygame.transform.smoothscale((pygame.image.load("pictures/space.jpg")),(1900,1000))

sun_image = pygame.transform.smoothscale((pygame.image.load("pictures/sun.png")), \
                (150, int((pygame.image.load("pictures/sun.png")).get_height() * \
                (150 / (pygame.image.load("pictures/sun.png")).get_width()))))

mercury_image = pygame.transform.smoothscale((pygame.image.load("pictures/mercury.png")), \
                (50, int((pygame.image.load("pictures/mercury.png")).get_height() * \
                (50 / (pygame.image.load("pictures/mercury.png")).get_width()))))

venus_image = pygame.transform.smoothscale((pygame.image.load("pictures/venus.png")), \
                (50, int((pygame.image.load("pictures/venus.png")).get_height() * \
                (50 / (pygame.image.load("pictures/venus.png")).get_width()))))

earth_image = pygame.transform.smoothscale((pygame.image.load("pictures/earth.png")), \
                (100, int((pygame.image.load("pictures/earth.png")).get_height() * \
                (100 / (pygame.image.load("pictures/earth.png")).get_width()))))

mars_image = pygame.transform.smoothscale((pygame.image.load("pictures/mars.png")), \
                (50, int((pygame.image.load("pictures/mars.png")).get_height() * \
                (50 / (pygame.image.load("pictures/mars.png")).get_width()))))

jupiter_image = pygame.transform.smoothscale((pygame.image.load("pictures/jupiter.png")), \
                (300, int((pygame.image.load("pictures/jupiter.png")).get_height() * \
                (300 / (pygame.image.load("pictures/jupiter.png")).get_width()))))

saturn_image = pygame.transform.smoothscale((pygame.image.load("pictures/saturn.png")), \
                (250, int((pygame.image.load("pictures/saturn.png")).get_height() * \
                (250 / (pygame.image.load("pictures/saturn.png")).get_width()))))

uranus_image = pygame.transform.smoothscale((pygame.image.load("pictures/uranus.png")), \
                (125, int((pygame.image.load("pictures/uranus.png")).get_height() * \
                (125 / (pygame.image.load("pictures/uranus.png")).get_width()))))

neptune_image = pygame.transform.smoothscale((pygame.image.load("pictures/neptune.png")), \
                (125, int((pygame.image.load("pictures/neptune.png")).get_height() * \
                (125 / (pygame.image.load("pictures/neptune.png")).get_width()))))

class Planet:
    SCALE = 175 / planet_data.AU    # 1AU = 100 pixels
    TIMESTEP = 3600*24  # 1 day

    def __init__(self,x,y,radius,color,mass,image=None):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.image = image
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self,win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
    
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))
                
            pygame.draw.lines(win, self.color, False, updated_points, 2)
        if self.image:
            image_rect = self.image.get_rect(center=(x, y))
            win.blit(self.image, image_rect)
        else:
            pygame.draw.circle(win, self.color, (x, y), self.radius)
        
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, (255,255,255))
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
    def attraction(self,other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = planet_data.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y,distance_x)
        force_x = math.cos(theta)*force
        force_y = math.sin(theta)*force
        return force_x, force_y

    def update_position(self,planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x,self.y))

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, planet_data.SUN['color'], planet_data.SUN['mass'],sun_image)
    sun.sun = True
    mercury = Planet(planet_data.MERCURY['orbital_distance'], 0, 10, planet_data.MERCURY['color'], planet_data.MERCURY['mass'],mercury_image)
    venus = Planet(planet_data.VENUS['orbital_distance'], 0, 13, planet_data.VENUS['color'],planet_data.VENUS['mass'],venus_image)
    earth = Planet(planet_data.EARTH['orbital_distance'], 0, 16, planet_data.EARTH['color'], planet_data.EARTH['mass'],earth_image)
    mars = Planet(planet_data.MARS['orbital_distance'], 0, 11, planet_data.MARS['color'], planet_data.MARS['mass'],mars_image)
    jupiter = Planet(planet_data.JUPITER['orbital_distance']/2.3, 0, 30, planet_data.JUPITER['color'], planet_data.JUPITER['mass'],jupiter_image)
    saturn = Planet(planet_data.SATURN['orbital_distance']/3.4, 0, 27, planet_data.SATURN['color'], planet_data.SATURN['mass'],saturn_image)
    uranus = Planet(planet_data.URANUS['orbital_distance']/5.7, 0, 20, planet_data.URANUS['color'], planet_data.URANUS['mass'],uranus_image)
    neptune = Planet(planet_data.NEPTUNE['orbital_distance']/7.8, 0, 20, planet_data.NEPTUNE['color'], planet_data.NEPTUNE['mass'],neptune_image)

    mercury.y_vel= planet_data.MERCURY['orbital_velocity']
    venus.y_vel = planet_data.VENUS['orbital_velocity']
    earth.y_vel = planet_data.EARTH['orbital_velocity']
    mars.y_vel = planet_data.MARS['orbital_velocity']
    jupiter.y_vel = planet_data.JUPITER['orbital_velocity']
    saturn.y_vel = planet_data.SATURN['orbital_velocity']
    uranus.y_vel = planet_data.URANUS['orbital_velocity']
    neptune.y_vel = planet_data.NEPTUNE['orbital_velocity']

    planets = [sun,earth,mercury,venus,mars,jupiter,saturn,uranus,neptune]

    while run:
        clock.tick(60)
        WIN.fill((0,0,0))
        WIN.blit(space_image,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.update_position(planets) 
            planet.draw(WIN)
        pygame.display.update()
    pygame.quit()
main()