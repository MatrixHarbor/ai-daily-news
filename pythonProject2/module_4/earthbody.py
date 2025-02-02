import math

N = 5
G = 6.67E-11
SUN = 3
#        x1 position y1 position vx velocity vy velocity m1 mass
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
sun =   [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
# plants = [earth,sun]
# print(plants[0])
t_total = 0
dt = 25000 # delta t
t = 157788000 # total simulation time

x1 = earth[0]
y1 = earth[1]
vx = earth[2]
vy = earth[3]
m1 = earth[4]

x0 = sun[0]
y0 = sun[1]
vx0 = sun[2]
vy0 = sun[3]
m0 = sun[4]

# print(vx,vy)
# print(x1)
# print(r1)
# print(m1,m0)

while t_total < t:
    # for plant in range(len(plants)-1):
        # print(plants[plant])

    dx = x1 - x0 # this is x position
    dy = y1 - y0 # this is y position
    r1 = (dx**2 + dy**2) ** 0.5 # this is the radius

    F = G*(m1*m0) / (r1**2) # calculate the F
    Fx = -F * (dx/r1) # Fx
    Fy = -F * (dy/r1) # Fy

    ax = Fx / m1
    ay = Fy / m1

    vx += ax*dt
    vy += ay*dt

    x1 += vx*dt
    y1 += vy*dt

    t_total += dt

print(f"{x1:.4e} {y1:.4e} {vx:.4e} {vy:.4e} {m1:.4e}")