import math

# Constants
G = 6.67E-11  # Gravitational constant
dt = 25000  # Time step in seconds
t = 157788000  # Total simulation time in seconds (approximately 5 years)

# Initial conditions for Earth and Sun [x position, y position, vx, vy, mass]
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]

# Extract initial conditions for Earth and Sun
x1, y1, vx, vy, m1 = earth  # Earth
x0, y0, vx0, vy0, m0 = sun  # Sun

# Total time for simulation
t_total = 0

# Simulation loop
while t_total < t:
    # Calculate the distance between the Earth and the Sun
    dx = x1 - x0
    dy = y1 - y0
    r1 = (dx ** 2 + dy ** 2) ** 0.5

    # Calculate the gravitational force
    F = G * (m1 * m0) / (r1 ** 2)

    # Calculate the force components
    Fx = -F * (dx / r1)  # Force in the x direction (attractive force, hence negative)
    Fy = -F * (dy / r1)  # Force in the y direction (attractive force, hence negative)

    # Calculate accelerations of Earth
    ax = Fx / m1
    ay = Fy / m1

    # Update velocities of Earth (Euler method)
    vx += ax * dt
    vy += ay * dt

    # Update positions of Earth (Euler method)
    x1 += vx * dt
    y1 += vy * dt

    # Increment total time
    t_total += dt

# Output the final position and velocity of Earth
print(f"Final position of Earth: x = {x1:.4e} m, y = {y1:.4e} m")
print(f"Final velocity of Earth: vx = {vx:.4e} m/s, vy = {vy:.4e} m/s")