# Planet_Simulation by Gierado Pham

## Planetary Motion Simulation

This project is a Python-based simulation of planetary motion in our solar system, using real-world data and physical principles. It calculates gravitational interactions between celestial bodies to model their orbits, velocities, and positions accurately. The simulation, visualized with Pygame, offers an interactive and scientific view of planetary dynamics based on up-to-date values.

### Assumptions:
- **Orbital Distance** Data for this parameter could not be obtained from NASA's HORIZONS API. Therefore, alternative credible sources were used for accurate data. The orbital distances of Jupiter, Saturn, Uranus, and Neptune were scaled down to fit all planets within the simulation window.
- **Orbital Velocity** To maintain accurate orbits despite the scaled-down distances, the orbital velocities of Jupiter, Saturn, Uranus, and Neptune were scaled up. This adjustment compensates for the reduced distances to avoid unrealistic gravitational interactions.
- **Orbit Shape** According to Kepler's Law of Planetary Motion, the planets' orbit should be more of an elliptical shape, but his simulation simplifies them to circular orbits for ease of visualization and computation.

### Key Features:
- **Real-world physics:** The simulation uses accurate planetary data—like mass, radius, orbital velocity, and distance from the Sun—to create realistic orbits.
- **Gravitational interactions:** Newton’s law of universal gravitation is at the heart of this simulation, calculating the forces between planets and adjusting their positions accordingly.
- **Visual representation:** Pygame is used to draw planets and their orbits, with careful scaling and centering to fit the solar system within the window.
- **Real-time updates:** Each planet’s position is updated based on its velocity and the gravitational forces acting on it, providing a dynamic, interactive experience.
- **Object-oriented design:** Planets are represented as objects, each with its own attributes (mass, radius, velocity) and behaviors, such as orbital motion.

### Technologies & Skills:
- **API Integration:** Connected to NASA’s HORIZONS API to fetch real-time planetary data, ensuring the simulation reflects the most accurate and current movements of the planets.
- **Python Libraries:**
  - **Pygame** for rendering planets and their orbits graphically.
  - **Requests** to pull planetary data from NASA’s HORIZONS API.
  - **Math** for precise gravitational force and orbital motion calculations.
- **Data Parsing:** Extracted planetary properties (mass, radius, orbital distance) from API responses using string manipulation and regular expressions.
- **Object-Oriented Programming (OOP):** Each planet is an object, with attributes like mass, radius, and velocity. The logic for gravitational forces and motion is encapsulated within each planet’s class.
- **Simulation Algorithms:** Developed algorithms to simulate gravitational forces and orbital mechanics, constantly updating the positions and velocities of planets in real time.

### Technical Skills Involved:
- **Modular Code Design:** Separated the simulation into modules for planetary data, simulation logic, and visualization.
- **Version Control:** Managed the project with Git and GitHub, making it easy to track changes and collaborate.
- **Debugging and Testing:** Extensively tested the gravitational calculations and orbital paths to ensure accuracy against real-world data.

### How to Run:
1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Run `Planet_Simulation.py` to launch the simulation and watch the planets move!

**Note:** Neptune will take approximately 3 minutes in the simulation to complete one orbit due to its large orbital distance and slower orbital velocity.


