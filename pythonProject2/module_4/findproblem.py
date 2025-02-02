import math

G = 6.67E-11
#        x1 position y1 position vx velocity vy velocity m1 mass
earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
sun =   [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
# plants = [earth,sun]
# print(plants[0])
t_total = 0
dt = 25000 # delta t
t = 157788000 # total simulation time

x1,y1,vx,vy,m1 = earth
x0,y0,vx0,vy0,m0 = sun

# print(vx,vy)
# print(x1)
# print(r1)
# print(m1,m0)

while t_total < t:
    # for plant in range(len(plants)-1):
        # print(plants[plant])




    x1 = earth[0] #This is the MISTAKE
    y1 = earth[1] #This is the MISTAKE

# because every time here, x1 will go back to earth[0] so is y1
# so x1 and y1 will also iterate 1 time the second time they go back to the origin



    r1 = (x1**2 + y1**2) ** 0.5

    F = G*(m1*m0) / (r1**2)
    Fx = -F * (x1/r1)
    Fy = -F * (y1/r1)

    ax = Fx / m1
    ay = Fy / m1

    vx += ax*dt
    vy += ay*dt

    x1 += vx*dt
    y1 += vy*dt

    t_total += dt

print(f"{x1:.4e} {y1:.4e} {vx:.4e} {vy:.4e} {m1:.4e}")