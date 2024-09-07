"""
Planet_Simulation.py

A simulation of planetary motions using real astronomical data. The simulation
applies gravitational force calculations to mimic orbital dynamics and uses Pygame 
to visually represent planets as they orbit around the Sun.

- Uses pygame for rendering planets and their orbits.
- Loads planet images to represent different celestial bodies.
- Implements gravitational physics using Newton's law of gravitation.

Author: Gierado Pham
Date: 2024-08-16
"""


# Importing necessary modules
import pygame
import math
import planet_data
pygame.init()

# Define pop-up window size
WIDTH, HEIGHT = 1900, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Setup font and caption
pygame.display.set_caption("Planet Simulation")
FONT = pygame.font.SysFont("comicsans", 16)

# Load background image
space_image = pygame.transform.smoothscale((pygame.image.load("pictures/space.jpg")),(1900,1000))

# Load and resize images for planets and the Sun.
# The images are scaled to fit within the simulation window while maintaining their aspect ratio.
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

# Setup celestial body calculations for position, gravitational force
class Planet:
    """
    Represents a planet or celestial body in the simulation.
    
    Attributes:
    - x, y: Position of the planet.
    - radius: Radius of the planet for drawing purposes.
    - color: Color of the planet if no image is provided.
    - mass: Mass of the planet, used in gravitational force calculations.
    - image: Optional image to represent the planet visually.
    - orbit: List of previous positions, used to draw the orbit path.
    - distance_to_sun: Distance from the planet to the sun, calculated dynamically.
    - x_vel, y_vel: Velocity components in x and y directions.
    """
    SCALE = 175 / planet_data.AU    # 1AU = 100 pixels
    TIMESTEP = 3600*24  # 1 day

    # Define parameters
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

    # Draw function will scale each planet to fit inside the pygame window
    def draw(self,win):
        """
        Draws the planet and its orbit on the window.

        - Positions are scaled according to the SCALE factor to fit the simulation window.
        - If the planet has an image, it is drawn. Otherwise, a colored circle represents it.
        """
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

    # Calculate gravitational force of attraction between sun and planets        
    def attraction(self,other):
        """
        Calculates the gravitational force exerted on this planet by another celestial body.
          
        - Uses Newton's law of gravitation to calculate the force magnitude.
        - The force is split into x and y components based on the angle between the two planets.
        
        Returns:
        - force_x, force_y: The force components in the x and y directions.
        """
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance
        
        # Gravitational Force Equation
        force = planet_data.G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y,distance_x)
        force_x = math.cos(theta)*force
        force_y = math.sin(theta)*force
        return force_x, force_y

    # Update position of planets based on gravitational force and orbital velocity
    def update_position(self,planets):
        """
        Updates the planet's position based on the gravitational forces from other planets.
        
        - Iterates through all other planets and calculates the net force acting on this planet.
        - Updates the planet's velocity based on the net force.
        - Uses the velocity to update the planet's position.
        - Appends the new position to the orbit list to track the orbit path.
        """
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            
            # Sum of the forces
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        # Final velocity and position of planets
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x,self.y))

# Running the simulation
def main():
    """
    Main loop of the simulation.
    
    - Initializes the celestial bodies (planets and the sun).
    - Starts the pygame window and runs the simulation until the user quits.
    - For each frame, the positions of the planets are updated, and they are drawn on the window.
    """
    run = True
    clock = pygame.time.Clock()

    # Extract necessary values from planet_data module
    sun = Planet(0, 0, 30, planet_data.SUN['color'], planet_data.SUN['mass'],sun_image)
    sun.sun = True
    mercury = Planet(planet_data.MERCURY['orbital_distance'], 0, 10, planet_data.MERCURY['color'], planet_data.MERCURY['mass'],mercury_image)
    venus = Planet(planet_data.VENUS['orbital_distance'], 0, 13, planet_data.VENUS['color'],planet_data.VENUS['mass'],venus_image)
    earth = Planet(planet_data.EARTH['orbital_distance'], 0, 16, planet_data.EARTH['color'], planet_data.EARTH['mass'],earth_image)
    mars = Planet(planet_data.MARS['orbital_distance'], 0, 11, planet_data.MARS['color'], planet_data.MARS['mass'],mars_image)
    jupiter = Planet(planet_data.JUPITER['orbital_distance'], 0, 30, planet_data.JUPITER['color'], planet_data.JUPITER['mass'],jupiter_image)
    saturn = Planet(planet_data.SATURN['orbital_distance'], 0, 27, planet_data.SATURN['color'], planet_data.SATURN['mass'],saturn_image)
    uranus = Planet(planet_data.URANUS['orbital_distance'], 0, 20, planet_data.URANUS['color'], planet_data.URANUS['mass'],uranus_image)
    neptune = Planet(planet_data.NEPTUNE['orbital_distance'], 0, 20, planet_data.NEPTUNE['color'], planet_data.NEPTUNE['mass'],neptune_image)

    mercury.y_vel= planet_data.MERCURY['orbital_velocity']
    venus.y_vel = planet_data.VENUS['orbital_velocity']
    earth.y_vel = planet_data.EARTH['orbital_velocity']
    mars.y_vel = planet_data.MARS['orbital_velocity']
    jupiter.y_vel = planet_data.JUPITER['orbital_velocity']
    saturn.y_vel = planet_data.SATURN['orbital_velocity']
    uranus.y_vel = planet_data.URANUS['orbital_velocity']
    neptune.y_vel = planet_data.NEPTUNE['orbital_velocity']

    planets = [sun,earth,mercury,venus,mars,jupiter,saturn,uranus,neptune]

    # Main simulation loop, runs continuously until the user closes the window
    while run:
        clock.tick(60)  # Limits the frame rate to 60 frames per second (FPS)
        WIN.fill((0, 0, 0))  # Clears the screen by filling it with black color
        WIN.blit(space_image, (0, 0))  # Draws the background space image

        # Event loop to check for user interaction, e.g., closing the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user clicks the 'X' button, stop the simulation
                run = False

        # Update the positions and draw each planet on the screen
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()  # Refresh the display with the updated positions of the planets

    # Quit pygame and close the window when the loop exits
    pygame.quit()
main()