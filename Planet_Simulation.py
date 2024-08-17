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

WHITE = (255, 255, 255)

FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    G = 6.6743e-11    # Gravitational constant or attraction between two objects
    TIMESTEP = 3600*24    # 1 day in seconds

    # Initiating the planet's properties
    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    # Accouting for the offset of the simulation window
    def draw(self, win, offset_x=0, offset_y=0, zoom=1):
        # Adjust the position of the planet for zoom and pan
        x = (self.x * self.SCALE * zoom) + WIDTH/2 + offset_x
        y = (self.y * self.SCALE * zoom) + HEIGHT/2 + offset_y

        # Update the orbit points to reflect the current zoom and pan
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                point_x, point_y = point
                point_x = (point_x * self.SCALE * zoom) + WIDTH / 2 + offset_x
                point_y = (point_y * self.SCALE * zoom) + HEIGHT / 2 + offset_y
                updated_points.append((point_x, point_y))

            # Draw the orbit trail
            pygame.draw.lines(win, self.color, False, updated_points, 2)

        # Draw the planet itself
        pygame.draw.circle(win, self.color, (int(x), int(y)), int(self.radius * zoom))
        
        # Draw the distance to the sun (only if it's not the sun itself)
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

            if not self.sun:
                distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
                win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

    # Calculating the force of attraction between two objects
    def attraction(self,other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance ** 2
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

    sun = Planet(0,0,30,SUN, 1.98892 * 10 **30)
    sun.sun = True
    mercury = Planet(.387*Planet.AU, 0, 10, MERCURY, 3.30 * 10 **23)
    venus = Planet(.723*Planet.AU, 0, 13, VENUS, 4.89 * 10 **24)
    earth = Planet(-1*Planet.AU, 0, 16, EARTH, 5.9742 * 10 **24)
    mars = Planet(-1.524*Planet.AU, 0, 11, MARS, 6.42 * 10 **23)
    jupiter = Planet(-2.203*Planet.AU, 0, 30, JUPITER, 1.90 * 10 **27)
    saturn = Planet(2.582*Planet.AU, 0, 27, SATURN, 5.68 * 10 **26)
    uranus = Planet(-2.701*Planet.AU, 0, 20, URANUS, 8.7 * 10 **25)
    neptune = Planet(2.947*Planet.AU, 0, 20, NEPTUNE, 10.2 * 10 **25)
    # pluto = Planet(-39.53*Planet.AU, 0, 5, PLUTO, 5.9742 * 10 **24)
#
    mercury.y_vel= -47.4 * 1000
#    venus = Planet(-.6794*Planet.AU, 0.2473*Planet.AU, 13, VENUS, 4.89 * 10 **24)
    venus.y_vel = -35.02 * 1000
#    earth = Planet(.7071*Planet.AU, 0.7071*Planet.AU, 16, EARTH, 5.9742 * 10 **24)
    earth.y_vel = 29.783 * 1000
#    mars = Planet(1.0776*Planet.AU, -1.0776*Planet.AU, 11, MARS, 6.42 * 10 **23)
    mars.y_vel = 24.077 * 1000
#    jupiter = Planet(1.347*Planet.AU,-5.03*Planet.AU, 30, JUPITER, 1.90 * 10 **27)
    jupiter.y_vel = 20.05 * 1000
#    saturn = Planet(9.25*Planet.AU, 2.48*Planet.AU, 27, SATURN, 5.68 * 10 **26)
    saturn.y_vel = -18.46 * 1000
#    uranus = Planet(18.11*Planet.AU,-17.49*Planet.AU, 20, URANUS, 8.7 * 10 **25)
    uranus.y_vel = 18.11 * 1000
#    neptune = Planet(30.047*Planet.AU, 0, 20, NEPTUNE, 10.2 * 10 **25)
    neptune.y_vel = -17.43 * 1000 
    #pluto = Planet(-39.53*Planet.AU, 0, 5, PLUTO, 5.9742 * 10 **24)

    #planets = [sun,earth,mercury,venus,mars,jupiter,saturn,uranus,neptune]
    planets = [sun,earth,mercury,venus,mars,jupiter,saturn,uranus,neptune]
    offset_x = 0  # Initialize the x offset for panning
    offset_y = 0  # Initialize the y offset for panning
    zoom = 1  # Initialize the zoom level
    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PLUS:
                    zoom += 0.1  # Zoom in
                elif event.key == pygame.K_MINUS:
                    zoom -= 0.1  # Zoom out
                elif event.key == pygame.K_LEFT:
                    offset_x += 20  # Pan left
                elif event.key == pygame.K_RIGHT:
                    offset_x -= 20  # Pan right
                elif event.key == pygame.K_UP:
                    offset_y += 20  # Pan up
                elif event.key == pygame.K_DOWN:
                    offset_y -= 20  # Pan down
        
        for planet in planets:
            planet.update_position(planets)  # This is the correct method call
            planet.draw(WIN, offset_x, offset_y, zoom)
        
        pygame.display.update()
    pygame.quit()

main()